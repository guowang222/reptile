from fake_useragent import UserAgent
import requests
from lxml import etree
from time import sleep

for i in range(1,6):
 
    print(f'========正在获取第{i}页数据=======')
    url = f'http://www.zongheng.com/rank/details.html?rt=1&d=1&p={i}'
    headers = {'User-Agent':UserAgent().chrome}
    resp = requests.get(url,headers =headers)

    # 构造etree对象
    e = etree.HTML(resp.text)

    names = e.xpath('//div[@class="rank_d_b_name"]/@title')
    for name in names:
        print(name)
    sleep(1)