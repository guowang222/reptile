import requests
from fake_useragent import UserAgent
import re

url = 'https://sports.qq.com/'
headers = {'User-Agent':UserAgent().chrome}
resp = requests.get(url,headers=headers)
regx = f'<li><a target="_blank" href=".+?" class=".*?">(.+?)</a></li>'
datas = re.findall(regx,resp.text)
for d in datas:
    print(d)