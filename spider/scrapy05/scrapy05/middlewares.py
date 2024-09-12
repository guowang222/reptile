from base64 import encode
from fake_useragent import UserAgent
from selenium import webdriver
from scrapy.http import HtmlResponse

class UserAgentDownloaderMiddleware:

    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', UserAgent().chrome)
        return None

    def process_response(self, request, response, spider):
        print(response.text)
        return response

class ProxyDownloaderMiddleware:

    def process_request(self, request, spider):
        # request.meta['proxy'] ='http://ip:port'
        # request.meta['proxy'] ='http://name:pwd@ip:port'
        request.meta['proxy'] ='http://139.224.211.212:8080'
        return None

    def process_response(self, request, response, spider):
        print(response.text)
        return response

class SeleniumDownloaderMiddleware:
    # def __init__(self) -> None:
    #     self.chrome = webdriver.Chrome(executable_path='../tools/chromedriver.exe')
    def process_request(self, request, spider):  
        spider.chrome.get(request.url)
        html = spider.chrome.page_source
        return HtmlResponse(url = request.url,body = html,request = request,encoding='utf-8')


