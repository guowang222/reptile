import scrapy


class XsSpider(scrapy.Spider):
    name = 'xs'
    allowed_domains = ['xbiquge.la']
    start_urls = ['https://www.xbiquge.la/10/10489/4535761.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        content = response.xpath('string(//div[@id="content"])').get()

        yield {
            'title':title,
            'content':content
        }
        next_url  = response.xpath('//div[@class="bottem1"]/a[4]/@href').get()

        yield scrapy.Request(response.urljoin(next_url))
