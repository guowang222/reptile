import requests
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers = {'User-Agent':UserAgent().chrome}
'''
"type":"type://ip:port"
"type":"type://username:password@ip:port"
'''
proxy = {
#   'http':'http://113.100.209.63:3128'
    'http':'http://398707160:j8inhg2g@114.117.238.188:16819'
}
resp = requests.get(url,headers =headers,proxies=proxy)
print(resp.text)