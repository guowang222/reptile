from urllib.request import Request,urlopen
from fake_useragent import UserAgent

url ='https://www.hupu.com/home/v1/news?pageNo=2&pageSize=50'
headers = {'User-Agent':UserAgent().chrome}
req = Request(url,headers = headers)
resp = urlopen(req)
print(resp.read().decode())

'''
静态
    访问地址栏里的数据就可以获取到想要的数据。 
动态
    访问地址栏里的数据就可以获取不到想要的数据。 
    解决方案：抓包
        打开浏览器的开发者工具- network-xhr,找到可以获取到数据的url访问即可
'''

# import ssl

# ssl._create_unverified_context()