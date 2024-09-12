from proxy_db import DB_Mongo
from proxy_fetcher import kuai_dai_li,yun_dai_li,all_world,zhi_ma_dai_li
from proxy_validata import validata_ip
from config import logging

def start():
    # 链接数据库
    db = DB_Mongo()
    # 下载IP
    '''
    for ip in yun_dai_li():
        logging.info(ip)
        # 验证IP
        if validata_ip(ip):
            # 通过验证后，保存IP
            db.insert(ip)
    for ip in kuai_dai_li():
        logging.info(ip)
        # 验证IP
        if validata_ip(ip):
            # 通过验证后，保存IP
            db.insert(ip)
    '''
    for ip in zhi_ma_dai_li():
        if validata_ip(ip):
            # 通过验证后，保存IP
            db.insert(ip)
    # 关闭DB链接
    db.close()

if __name__ =="__main__":
    start()