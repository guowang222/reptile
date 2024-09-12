import scrapy
from scrapy_splash import SplashRequest

class Douban1Spider(scrapy.Spider):
    name = 'douban3'
    allowed_domains = ['douban.com']

    def start_requests(self):
        url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
        
        lua='''
        function main(splash,args)
            splash:go(args.url)
            splash:wait(1.5)
            return splash:html()
        end
        '''
        yield SplashRequest(url,callback=self.parse,args={'lua_source':lua},endpoint='execute')
    def parse(self, response):
        with open('a2.html','wb') as f:
            f.write(response.body)
