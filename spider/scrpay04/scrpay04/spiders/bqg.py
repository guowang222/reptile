import scrapy


class BqgSpider(scrapy.Spider):
    name = 'bqg'
    allowed_domains = ['xbiquge.la']
    start_urls = ['https://www.xbiquge.la/10/10489/']

    def parse(self, response):
        title = response.xpath('//div[@id="list"]/dl/dd[2]/a/text()').get()
        next_url = response.xpath('//div[@id="list"]/dl/dd[2]/a/@href').get()
        print(next_url,'================')
        yield scrapy.Request(response.urljoin(next_url),meta={'title':title},callback=self.parse_info)

    def parse_info(self,response):
        title = response.request.meta.get('title')
        print(title,'==========================')