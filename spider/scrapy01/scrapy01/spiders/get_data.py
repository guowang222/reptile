import scrapy
from scrapy.selector import Selector

class GetDataSpider(scrapy.Spider):
    name = 'get_data'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # 获取title  
        # extract() getall() 从选择器里面提取多条数据 
        # extract_first() get() 从选择器里面提取单条数据
        # 方式1:xpath  与css 2选1
        print('='*5,'xpath()','='*5)
        title = response.selector.xpath('//title/text()').extract()
        print(title)
        title2 = response.selector.xpath('//title/text()').getall()
        print(title2)
        title3 = response.selector.xpath('//title/text()').extract_first()
        print(title3)
        title4 = response.selector.xpath('//title/text()').get()
        print(title4)
        title5 = response.xpath('//title/text()').get()
        print(title5)
        # 方式2：css 与xpath 2选1
        print('='*5,'css()','='*5)
        c1 = response.css('title::text').extract_first()
        c2 = response.css('title').xpath('./text()').get()      # 可以混合使用
        print(c1)
        print(c2)
        # 方式3：re  推荐会
        print('='*5,'re()','='*5)
        r1 = response.selector.re('<title>(.+)</title>')  # findall()
        s1 = Selector(response = response)  # 手动创建selector
        r2 = s1.re('<title>(.+)</title>')
        print(r1)
        print(r2)
