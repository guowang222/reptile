import scrapy
from scrpay04.settings import COOKIE

class KdlSpider(scrapy.Spider):
    name = 'kdl'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/usercenter/']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0],cookies=COOKIE)

    def parse(self, response):
        print(response.text)
