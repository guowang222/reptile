import scrapy

class Zol1Spider(scrapy.Spider):
    name = 'zol3'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9630_116592_2.html']

    def parse(self, response):
        img_url = response.xpath('//img[@id="bigImg"]/@src').get()
        img_name = response.xpath('string(//h3)').get().strip().replace('\r\n\t\t','')
        yield {
            'img_url':img_url,
            'img_name':img_name
        }
        next_url = response.xpath('//a[@id="pageNext"]/@href').get()
        if next_url.find('javascript') ==-1:
            # full_url = f'https://desk.zol.com.cn/{next_url}'
            full_url = response.urljoin(next_url)
            yield scrapy.Request(full_url)
