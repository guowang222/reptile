import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Xs4Spider(CrawlSpider):
    name = 'xs4'
    allowed_domains = ['xbiquge.la']
    start_urls = ['https://www.xbiquge.la/10/10489/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//div[@id="list"]/dl/dd[2]/a'),
        callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[4]'),
        callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//h1/text()').get()
        content = response.xpath('string(//div[@id="content"])').get()
        
        yield {
            'title':title,
            'content':content
        }

