import scrapy
from json import loads

class CwlSpider(scrapy.Spider):
    name = 'cwl'
    allowed_domains = ['cwl.gov.cn']
    # start_urls = ['http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=30']
    def start_requests(self):
        url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=30'
        headers ={
            'Referer':'http://www.cwl.gov.cn/kjxx/ssq/kjgg/'
        }
        yield scrapy.Request(url,headers=headers)

    def parse(self, response):
        print(response.text)

        data = loads(response.text)
        for d in data.get('result'):
            yield {
                'code':d.get('code'),
                'red':d.get('red'),
                'blue':d.get('blue')
            }