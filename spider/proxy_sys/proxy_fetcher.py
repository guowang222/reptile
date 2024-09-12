from request_util import WebRequest
from config import logging
import re

def kuai_dai_li():
    req = WebRequest()
    for i in range(1,6):
        url = f'https://www.kuaidaili.com/free/inha/{i}/'
        req.do_get(url)
        e = req.get_tree()
        ips = e.xpath('//tr/td[1]/text()')
        ports = e.xpath('//tr/td[2]/text()')
        _types = e.xpath('//tr/td[4]/text()')
        for i,p,t in zip(ips,ports,_types):
            #logging.info(f'{t.lower()}://{i}:{p}')
            yield {'ip':i,'port':p,'_type':t.lower(),'full_url':f'{t.lower()}://{i}:{p}'}

def yun_dai_li():
    req = WebRequest()
    for i in range(1,6):
        url = f'http://www.ip3366.net/?stype=1&page={i}'
        req.do_get(url)
        e = req.get_tree()
        ips = e.xpath('//tr/td[1]/text()')
        ports = e.xpath('//tr/td[2]/text()')
        _types = e.xpath('//tr/td[4]/text()')
        for i,p,t in zip(ips,ports,_types):
            # logging.info(f'{t.lower()}://{i}:{p}')
            yield {'ip':i,'port':p,'_type':t.lower(),'full_url':f'{t.lower()}://{i}:{p}'}
def all_world():
    url = 'https://ip.jiangxianli.com/?page=1'
    req = WebRequest()
    req.do_get(url)
    text = req.get_text()
    count,limit = re.findall('count: "(\d+)", limit: "(\d+)"',text)[0]
    page = (int(count) // int(limit)) + 1 
    for i in range(1,page):
        url = f'https://ip.jiangxianli.com/?page={i}'
        req.do_get(url)
        e = req.get_tree()
        ips = e.xpath('//tr/td[1]/text()')
        ports = e.xpath('//tr/td[2]/text()')
        _types = e.xpath('//tr/td[4]/text()')
        full_urls = e.xpath('//tr/td[last()]/button[1]/@data-url')
        for i,p,t,f in zip(ips,ports,_types,full_urls):
            # logging.info(f'{t.lower()}://{i}:{p}')
            yield {'ip':i,'port':p,'_type':t.lower(),'full_url':f}
def zhi_ma_dai_li():
    url = 'http://webapi.http.zhimacangku.com/getip?num=10&type=2&pro=&city=0&yys=0&port=1&pack=169352&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    req = WebRequest()
    req.do_get(url)
    json = req.get_json()

    for d in json.get('data'):
        yield {'ip':d.get('ip'),'port':d.get('port'),'_type':'http','full_url':f'http://{d.get("ip")}:{d.get("port")}'}

if __name__ == '__main__':
    # kuai_dai_li()
    # yun_dai_li()
    # all_world()
    pass