import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq

url = 'https://www.qidian.com/all'
headers= {'User-Agent':UserAgent().chrome}
resp = requests.get(url,headers=headers)

# 构造Pyquery对象
doc = pq(resp.text)

all_a = doc('[data-eid="qd_B58"]')
print(all_a)

for i in range(len(all_a)):     # pyquery
    print(all_a.eq(i).text())
print('-----------------------------------------')
for a in all_a: # element
    print(a.text)

print(type(all_a.eq(1)))
print(type(all_a[1]))