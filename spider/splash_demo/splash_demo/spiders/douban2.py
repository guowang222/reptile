import scrapy
from scrapy_splash import SplashRequest

class Douban1Spider(scrapy.Spider):
    name = 'douban2'
    allowed_domains = ['douban.com']

    def start_requests(self):
        url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
        yield SplashRequest(url,callback=self.parse,args={'wait':2})
    def parse(self, response):
        with open('a1.html','wb') as f:
            f.write(response.body)
