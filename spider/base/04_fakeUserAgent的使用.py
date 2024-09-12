from urllib.request import urlopen
from urllib.request import Request
from fake_useragent import UserAgent

ua = UserAgent()

url = 'http://httpbin.org/get'

headers = {
    'User-Agent':ua.opera
}
req = Request(url,headers=headers)
resp = urlopen(req)
print(resp.read().decode())