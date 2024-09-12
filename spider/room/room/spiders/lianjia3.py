import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule

class LianjiaSpider(RedisCrawlSpider):
    name = 'lianjia3'
    allowed_domains = ['lianjia.com']
    redis_key = 'room:start_urls'
    page_no = 2
    # start_urls = ['https://bj.lianjia.com/ershoufang/pg1/']

    rules = (
        # follow all links
        Rule(LinkExtractor(restrict_xpaths='//div[@class="info clear"]/div[@class="title"]/a'), callback='parse_info', follow=True),
    )
    def parse_info(self, response):
        total = response.xpath("//span[@class='total']/text()").get()
        community_name = response.xpath('//div[@class="communityName"]/a[1]/text()').get()
        area_name = response.xpath('string(//div[@class="areaName"]/span[2])').get()

        base = response.xpath('//div[@class="base"]/div[@class="content"]/ul')
        room_type = base.xpath('./li[1]/text()').get()
        room_lou_ceng = base.xpath('./li[2]/text()').get()
        room_area = base.xpath('./li[3]/text()').get()
        room_chao_xiang = base.xpath('./li[7]/text()').get()
        room_zhuang_xiu = base.xpath('./li[9]/text()').get()
        room_gong_nuan = base.xpath('./li[last()-1]/text()').get()
        room_dian_ti = base.xpath('./li[last()]/text()').get()

        yield {
            "total":total,
            "community_name":community_name,
            "area_name":area_name,
            "room_type":room_type,
            "room_lou_ceng":room_lou_ceng,
            "room_area":room_area,
            "room_chao_xiang":room_chao_xiang,
            "room_zhuang_xiu":room_zhuang_xiu,
            "room_gong_nuan":room_gong_nuan,
            "room_dian_ti":room_dian_ti
        }
        yield scrapy.Request(f'https://bj.lianjia.com/ershoufang/pg{self.page_no}/')
        self.page_no += 1

