import redis # pip install redis
from pymongo import MongoClient
from json import loads

# 连接Redis数据库
r_client = redis.Redis(host='localhost',port=6379,db=0)
# 连接Mongo数据库
m_client = MongoClient()
# 获取指定的集合
lianjia = m_client.room.lianjia
# 获取数据
while True:
    try:
        s,d = r_client.blpop(['lianjia3:items'],timeout=2)
    except Exception as e:
        # 关闭连接
        m_client.close()
        r_client.close()
    # 转换数据
    data = loads(d)
    print(data)
    # 保存数据
    lianjia.insert_one(data)


