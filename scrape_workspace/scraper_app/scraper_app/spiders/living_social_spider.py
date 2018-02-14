import scrapy
from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(scrapy.Spider):
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["http://www.livingsocial.com/cities/15-san-francisco"]

    deals_list_xpath = "//li[@dealid]"
