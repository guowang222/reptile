from urllib.request import Request,build_opener
from fake_useragent import UserAgent

url ='https://www.kuaidaili.com/usercenter/overview'
headers = {
    'User-Agent':UserAgent().chrome,
    'Cookie':'channelid=0; sid=1621786217815170; _ga=GA1.2.301996636.1621786363; _gid=GA1.2.699625050.1621786363; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1621786363,1621823311; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1621823382; sessionid=48cc80a5da3a451c2fa3ce682d29fde7'
}
req = Request(url,headers= headers)
opener = build_opener()
resp = opener.open(req)

print(resp.read().decode())
