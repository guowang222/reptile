import scrapy

class BaiduSpider(scrapy.Spider):
    name = 'baidu'  # 爬虫的名字，唯一， 必须写的
    allowed_domains = ['baidu.com'] # 允许爬取的域名, 不是必须写的
    start_urls = ['http://www.baidu.com/']  # 从哪个Url地址开始获取数据

    def parse(self, response):  # 当请求访问成功以后，会有一个响应。这个parse就是 默认 处理响应的函数
        print(response.text)
        


# scrapy startproject project_name
# 切换到项目目录里
# scrapy genspider spider_name  spider_domains
# scrapy crawl spider_name   运行代码时，环境路径在项目里面