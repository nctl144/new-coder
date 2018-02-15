import scrapy

from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose

from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(scrapy.Spider):
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["https://www.livingsocial.com/local/san-francisco"]

    deals_list_xpath = '//figure[@class="card-ui cui-c-udc cui-c-udc-featured-list"]'

    item_fields = {
        'title': './a/div[@class="cui-content c-bdr-gray-clr"]/div[@class="cui-udc-details"]/div[@class="cui-udc-title c-txt-black two-line-ellipsis"]/text()',
        'link': './a/attribute/href',
        'location': './/a/div[@class="cui-content c-bdr-gray-clr"]/div[@class="cui-udc-details"]/div[@class="cui-udc-top-row"]/div[@class="cui-udc-left-one"]/div[@class="cui-location cui-truncate c-txt-gray-dk cui-has-distance"]/span/text()',
        'original_price': './/a/div[@class="cui-content c-bdr-gray-clr"]/div[@class="cui-udc-details"]/div[@class="cui-udc-bottom-row"]/div[@class="cui-udc-right-two"]/div[@class="cui-price"]/s/text()',
        'price': './/a/div[@class="cui-content c-bdr-gray-clr"]/div[@class="cui-udc-details"]/div[@class="cui-udc-bottom-row"]/div[@class="cui-udc-right-two"]/div[@class="cui-price"]/span/text()',
        'items_sold': './/a/div[@class="cui-content c-bdr-gray-clr"]/div[@class="cui-udc-details"]/div[@class="cui-udc-bottom-row"]/div[@class="cui-udc-left-two"]/div[@class="cui-quantity-bought c-txt-gray-dk"]/text()'
    }

    def parse(self, response):
        selector = Selector(response)

        for deal in selector.xpath(self.deals_list_xpath):
            loader = ItemLoader(item=LivingSocialDeal(), selector=deal)

            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            for field, path in self.item_fields.iteritems():
                loader.add_xpath(field, path)
            yield loader.load_item()
