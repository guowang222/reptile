from urllib.request import Request,build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url = 'http://httpbin.org/get'
headers = {'User-Agent':UserAgent().chrome}
req = Request(url,headers=headers)
# 创建一个可以使用代理的控制 

# 共享代理
# handler = ProxyHandler({'type':'ip:port'})
# handler = ProxyHandler({'http':'110.18.152.229:9999'})

# 独享代理
# handler = ProxyHandler({'type':'user:pwd@ip:port'})
handler = ProxyHandler({'http':'398707160:j8inhg2g@114.117.236.72:16819'})

# 传递到opener
opener = build_opener(handler)
resp = opener.open(req)
print(resp.read().decode())

'''
快代理
https://www.kuaidaili.com

云代理
http://www.ip3366.net

无忧代理
http://www.data5u.com/

66ip 代理
http://www.66ip.cn

站大爷
https://www.zdaye.com/FreeIPList.html

讯代理
http://www.xdaili.cn/

蚂蚁代理
http://www.mayidaili.com/free

89免费代理
http://www.89ip.cn/

全网代理
http://www.goubanjia.com/buy/high.html

开心代理
http://ip.kxdaili.com/

'''