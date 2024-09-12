from urllib.request import Request,build_opener
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor

login_url ='https://www.kuaidaili.com/login/'

args = {
    'username':'398707160@qq.com',
    'passwd':'123456abc'
}
headers = {
    'User-Agent':UserAgent().chrome
}
req = Request(login_url,headers= headers,data = urlencode(args).encode())
# 创建一个可以保存cookie的控制器对象
handler = HTTPCookieProcessor()
# 构造发送请求的对象
opener = build_opener(handler)
#  登录
resp = opener.open(req)

'''
-------------------------上面已经登录好----------------------------------
'''

index_url ='https://www.kuaidaili.com/usercenter/overview'
index_req = Request(index_url,headers =headers)
index_resp = opener.open(index_req)

print(index_resp.read().decode())

