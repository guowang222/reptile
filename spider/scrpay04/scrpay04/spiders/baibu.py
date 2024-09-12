import scrapy


class BaibuSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url)
    def parse(self, response):
        print('访问了百度!!!')
        # dont_filter = True  不去重 
        # Request 对象默认是去重URL地址。想要不去重 dont_filter = True
        # strat_urls 是去重的
        yield scrapy.Request('http://www.baidu.com/')
        # yield scrapy.Request('http://www.baidu.com/',dont_filter= True)