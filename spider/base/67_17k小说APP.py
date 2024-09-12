'''
http://api.17k.com/v2/book/3325872/chapter/44158517/content?app_key=4037465544
http://api.17k.com/v2/book/3325872/chapter/44167791/content?app_key=4037465544
'''
from time import sleep
import requests

url = 'https://api.17k.com/v2/book/3325872/volumes?app_key=4037465544'

headers = {
    'User-Agent':'okhttp/3.2.0'
}
resp = requests.get(url,headers =headers)
with open('大唐：开局绑架李世民.txt','w',encoding='utf-8') as f:

    for i in resp.json().get('data').get('volumes')[0].get('chapters'):
        id = i.get('chapter_id')
        info_url =f'http://api.17k.com/v2/book/3325872/chapter/{id}/content?app_key=4037465544'
        name = i.get('chapter_name')
        info_resp = requests.get(info_url,headers = headers)
        data = info_resp.json().get('data').get('content')
        f.write(name)
        f.write('\n')
        f.write(data)
        f.write('\n')
        sleep(1)
        print(f'正在下载:{name}')
