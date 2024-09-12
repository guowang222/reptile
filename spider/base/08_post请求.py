from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode

url = 'https://www.21wecan.com/rcwjs/searchlist.jsp'
headers = {'User-Agent':UserAgent().chrome}
args={
    'searchword':'人才'
}
f_data = urlencode(args)
req = Request(url,headers=headers,data=f_data.encode()) # 如果传送了data参数，就会成为post请求!
resp = urlopen(req)
print(resp.read().decode())