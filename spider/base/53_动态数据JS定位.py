import requests
import os
from time import sleep
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

hero_js = requests.get('https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js',headers= header)
for hero in hero_js.json().get('hero'):
    id = hero.get('heroId')
    hero_name = hero.get('name')
    url = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{id}.js'
    js_resp = requests.get(url,headers= header)
    for sk in js_resp.json().get('skins'):
        file_name = sk.get('name').replace(' ','_')
        img_url = sk.get('mainImg')
        chromas = sk.get('chromas')
        if chromas =='0':
            img_resp = requests.get(img_url,headers= header)
            sleep(1)
            print(f'正在下载：{file_name} 图片')
            file_dir = f'imgs/{hero_name}'

            if not os.path.exists(file_dir):
                os.mkdir(file_dir)
            with open(f'imgs/{hero_name}/{file_name}.png','wb') as f :
                f.write(img_resp.content)

