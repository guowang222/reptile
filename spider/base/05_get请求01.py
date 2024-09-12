from urllib.request import urlopen,Request
from fake_useragent import UserAgent
from urllib.parse import quote

args =input('请输入要搜索的内容:')
ua = UserAgent()
url = f'https://www.baidu.com/s?wd={quote(args)}'
headers = {
    'User-Agent':ua.chrome
}
req = Request(url,headers = headers)
resp = urlopen(req)
print(resp.read().decode())