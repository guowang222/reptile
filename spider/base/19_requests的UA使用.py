import requests
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers = {'User-Agent':UserAgent().chrome}
resp = requests.get(url,headers =headers)
print(resp.text)