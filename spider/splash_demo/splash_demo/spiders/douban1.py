import scrapy


class Douban1Spider(scrapy.Spider):
    name = 'douban1'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=']
    
    def parse(self, response):
        with open('a0.html','wb') as f:
            f.write(response.body)
