from urllib.request import parse_http_list, urlopen,Request
from fake_useragent import UserAgent
from urllib.parse import urlencode

args =input('请输入要搜索的内容:')
parms ={
    'wd':args
}
ua = UserAgent()
# url = f'http://www.baidu.com/s?{urlencode(parms)}'

url = f'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&{urlencode(parms)}&oq=%25E5%25B0%259A%25E5%25AD%25A6%25E5%25A0%2582&rsv_pq=8ee83c4f000b323c&rsv_t=01e3%2BJpvwQfSqmdpkDAvAw2Dfv5WKdK6Qkwlj5Uc6sOejxnQJdl3zO3SChU&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=8&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_btype=t&inputT=335131&rsv_sug4=335473'

# print(url)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
req = Request(url )
resp = urlopen(req)
print(resp.read().decode())