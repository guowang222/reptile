from fake_useragent import UserAgent
import requests
# pip install jsonpath
import json
from jsonpath import jsonpath

url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=60&limit=20&strategy=1&ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}'
header = {'User-Agent':UserAgent().chrome}
resp = requests.get(url,headers=header)

# obj = json.loads(resp.text)
# titles = jsonpath(obj,'$..title') # 表达式 从头开写
# ids = jsonpath(obj,'$..cms_id')


titles = jsonpath(resp.json(),'$..title') # 表达式 从头开写
ids = jsonpath(resp.json(),'$..cms_id')

for id,title in zip(ids, titles):
    print(f'{id}:{title}')

# obj.get('data').get('list')[1].get('title')