import scrapy
from scrapy import signals
from selenium import webdriver

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print(response.text)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaiduSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.chrome = webdriver.Chrome(executable_path='../tools/chromedriver.exe')
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed) 
        # connect里的参数 
        # 1. 处罚事件后用哪个函数处理
        # 2. 捕捉哪个事件
        return spider


    def spider_closed(self, spider):
        spider.chrome.close()