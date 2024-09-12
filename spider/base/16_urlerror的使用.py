from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

url = 'http://www.sxtwerwf1jojhofsaf.cn/sadfa/sdfs14'
headers = {'User-Agent':UserAgent().chrome}
req = Request(url,headers = headers)
try:
    resp = urlopen(req)
    print(resp.read().decode())
except URLError as e:
    # print(e)
    if e.args:
        print(e.args[0].errno)
    else:
        print(e.code)
print('爬取完成')