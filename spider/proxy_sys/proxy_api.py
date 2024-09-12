# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI
from proxy_db import DB_Mongo
from proxy_validata import validata_ip

app = FastAPI()

@app.get('/')
def index():
    return {'Hello':'Python'}

@app.get('/get')
def get_proxy(_type:str):
    db = DB_Mongo()
    num = db.count(_type)
    if num == 0:
        return {'msg':'no IP'}
    flag = False
    while not flag:
        item = db.get(_type)
        flag = validata_ip(item)
        if not flag:
            db.delete_ip(item)
            if db.count(_type) == 0:
                return {'msg':'no IP'}
    del item['_id']
    db.close()
    return item

@app.get('/count') 
def get_count(_type:str):
    db = DB_Mongo()
    print(_type)
    data = {'count':db.count(_type)}
    print(data)
    db.close()
    return data

# 启动的命令是： uvicorn proxy_api:app --reload