from pymongo import MongoClient
import hashlib
from config import logging
from random import randint

class DB_Mongo:
    def __init__(self,host:str = 'localhost',port:int = 27017) -> None:
        self.client = MongoClient(host = host,port = port)
        self.proxy = self.client.proxy
        self.ip = self.proxy.ip
        self.fingerprint = self.proxy.fingerprint

    def insert(self,data:dict):
        '''
            增加数据
        '''
        ip = data.get('ip')
        f = hashlib.md5(ip.encode()).hexdigest()
        if not self.exists_fingerprint({'ip':f}):
            self.ip.insert_one(data)    
            self.fingerprint.insert_one({'ip':f})
            logging.debug(f'{data.get("ip")} 保存成功！')
        else:
            logging.debug(f'{data.get("ip")} 已存在！')

    def get(self,_type:str = 'http'):
        '''
            获取IP
        '''
        count = self.count(_type)
        if count == 0:
            return None
        elif count == 1:
            return self.ip.find_one({'_type':_type})
        else:
            num = randint(0, count-1)   # 随机生成数字，用来指定要获取第几个IP.
            return self.ip.find({'_type':_type}).limit(1).skip(num)[0]

    def count(self,_type:str = 'http'):
        '''
            统计IP数量
        '''
        
        return self.ip.count_documents({'_type':_type})

    def delete_ip(self,data:dict):
        '''
            删除IP
        '''
        self.ip.delete_one(data)
        logging.info(f'删除IP: {data.get("ip")}')

    def exists_fingerprint(self,data:dict):
        '''
            验证IP是否存在
        '''
        if self.fingerprint.count_documents(data) :
            logging.info('已经存在')
            return True
        else:
            return False
    def close(self):
        self.client.close()

if __name__ =='__main__':
    db = DB_Mongo()
    # db.insert({'ip':'127.0.0.2','port':'3306','_type':'http','full_url':'http://127.0.0.2:3306'})
    # ip  = db.get(_type='http')
    # logging.info(f'获取到了 {ip}')
    # db.delete_ip({'ip':'127.0.0.2'})
    # ip  = db.get(_type='http')
    # logging.info(f'获取到了 {ip}')
    # db.close()
    print(db.count('http'))
    # print(db.ip.count_documents({'_type':'http'}))
