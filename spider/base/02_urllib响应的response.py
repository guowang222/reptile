# urllib
from urllib.request import urlopen

url = 'http://www.baidu.com/'
resp = urlopen(url) # 发送请求，并将结果返回给resp

print(resp.read())  # 读取数据
print(resp.getcode())   # 为了判断是否要处理请求的结果
print(resp.geturl())    # 为了记录访问记录，避免2次访问，导致出现重复数据
print(resp.info())      # 响应头的信息，取到里面有用的数据
