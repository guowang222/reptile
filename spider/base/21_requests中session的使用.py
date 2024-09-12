import requests
from fake_useragent import UserAgent

login_url ='https://www.kuaidaili.com/login/'
args = {
    'username':'398707160@qq.com',
    'passwd':'123456abc'
}
headers = {'User-Agent':UserAgent().chrome}
session = requests.Session()
resp = session.post(login_url,data= args,headers =headers)
'''
-----------------------上面已经登录好---------------------------
'''
index_url ='https://www.kuaidaili.com/usercenter/overview'
index_resp = session.get(index_url,headers =headers)
print(resp.text)