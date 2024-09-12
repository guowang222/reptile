from splash_demo.settings import SPIDER_MIDDLEWARES
import scrapy
from scrapy_splash import SplashRequest

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    # start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        yield SplashRequest('http://www.baidu.com',callback=self.parse)

    def parse(self, response):
        print(response.text)
