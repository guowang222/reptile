# urllib
from urllib.request import urlopen

url = 'http://www.baidu.com/'
resp = urlopen(url) # 发送请求，并将结果返回给resp
print(resp.read().decode())
