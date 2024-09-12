from urllib.request import Request,build_opener
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers = {'User-Agent':UserAgent().chrome}
req = Request(url,headers= headers)
opener = build_opener()
resp = opener.open(req)
print(resp.read().decode())