import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['kuaidaili.com']
    
    def start_requests(self):
        url = 'https://www.kuaidaili.com/login/'
        data = {
            'login_type': '1',
            'username': '398707160@qq.com',
            'passwd': '123456abc',
        }
        yield scrapy.FormRequest(url,formdata=data)
    def parse(self, response):
        # print(response.text)
        yield scrapy.Request('https://www.kuaidaili.com/usercenter/overview/',callback=self.parse_info)

    def parse_info(self,response):
        print(response.text)
        #  cookie默认是开启的，如果需要不再保存cookie，可以去settings中关闭