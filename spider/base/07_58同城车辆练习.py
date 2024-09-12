from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import quote
from time import sleep

args = input('请输入品牌：')
for page in range(1,4):
    url =f'https://bj.58.com/ershouche/pn{page}/?key={quote(args)}'
    sleep(1)
    print(url)
    headers = {'User-Agent':UserAgent().chrome}
    req =  Request(url,headers = headers)
    resp = urlopen(req)
    # print(resp.read().decode())
    print(resp.getcode())