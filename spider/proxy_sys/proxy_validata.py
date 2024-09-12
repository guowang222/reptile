from request_util import WebRequest
from config import logging

def validata_ip(proxy:dict) -> bool:
    http_url = 'http://httpbin.org/get'
    https_url = 'https://httpbin.org/get'
    _type = proxy.get('_type')
    ip = proxy.get('ip')
    full_url = proxy.get('full_url')
    req = WebRequest()
    try:
        if 'http' == _type:
            req.do_get(http_url,proxies = {_type:full_url},timeout = 3)
        elif 'https' == _type:
            req.do_get(https_url,proxies = {_type:full_url},timeout = 3)
    except Exception as  e:
        logging.info(e)
        logging.info('IP 超时！！')
        return False
    if req.resp:
        origin_ip = req.get_json().get('origin')
        flag = origin_ip.find(ip)
        if flag != -1:
            logging.info('IP  成功')
            return True
        else:
            logging.info('IP 失败')
            return False
    else:
        logging.info('IP 失败')
        return False

if __name__ == '__main__':
    print(validata_ip({'ip':'51.83.130.27','port':'3128','_type':'http','full_url':'http://51.83.130.27:3128'}))