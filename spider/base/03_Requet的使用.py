from urllib.request import urlopen
from urllib.request import Request
from random import choice

# url = 'http://www.baidu.com/'
url = 'http://httpbin.org/get'

user_agent_list=[
    'ua1','ua2','ua3'
]

headers = {
    'User-Agent':choice(user_agent_list)
}
req = Request(url,headers=headers)
resp = urlopen(req)
# print(resp.getcode())
print(resp.read().decode())