import scrapy
from scrapy01.items import MovieItem

class SaveDataSpider(scrapy.Spider):
    name = 'save_data'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        titles = response.xpath('//a/span[@class="title"][1]/text()').getall()
        stars = response.xpath('//span[@class="rating_num"]/text()').getall()


        # with open('movie.txt','w',encoding='utf-8') as f:
        #     for t,s in zip(titles,stars):
        #         f.write(f'{t},{s}\n')

        # for t,s in zip(titles,stars):
        #     yield {
        #         'title':t,
        #         'star':s
        #     }
 
        for t,s in zip(titles,stars):
            item = MovieItem()
            item['title'] = t
            item['star']  = s
            yield item 
        '''
        给pipeline推送参数的方式 ： dict item（自己定义）
        '''