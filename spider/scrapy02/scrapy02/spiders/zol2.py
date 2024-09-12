import scrapy

class Zol1Spider(scrapy.Spider):
    name = 'zol2'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9630_116592_2.html']

    def parse(self, response):
        img_url = response.xpath('//img[@id="bigImg"]/@src').get()
        yield {
            'img_url':img_url
        }
