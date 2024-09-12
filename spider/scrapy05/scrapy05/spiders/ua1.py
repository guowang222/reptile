import scrapy


class Ua1Spider(scrapy.Spider):
    name = 'ua1'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print(response.text)
        pass
