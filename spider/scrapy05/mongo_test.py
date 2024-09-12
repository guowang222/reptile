from pymongo import MongoClient

# 获取链接
c1 = MongoClient('localhost',27017)
c2 = MongoClient('mongodb://localhost:27017')
print(c1 ==c2)
# 获取数据库实例
db = c1.sxt
db2 = c1["sxt"]
print(db ==db2)
# 获取集合
p1 = db.person
p2 = db['person']
print(p1 == p2)

def add_data():
    d = {'name':'貂蝉','age':20,'country':'群英'}
    # p2.insert_one(d)
    p2.save(d)
def update_data():
    # p1.update({'name':'貂蝉'},{'name':'孙尚香'})
    p1.update({'name':'吕布'},{'$set':{'name':'奉贤'}})
def delete_data():
    p1.delete_one({'name':'孙尚香'})

def show_data():
    # 操作数据
    for p in p1.find():
        print(p)

def show_only():
    d = p1.find_one()
    print(d)

def show_page():
    for p in p1.find().limit(2).skip(2):
        print(p)

def show_agg():
    rs = p1.aggregate([{"$group":{"_id":"$country","counter":{"$sum":1}}}])
    for r in rs:
        print(r)

def show_sort():
    p = p1.find().sort("age",1)
    for t in p:
        print(t)
        
if __name__ == "__main__":
    # add_data()
    # update_data()
    # delete_data()
    # show_data()
    # show_only()
    # show_page()
    # show_agg()
    show_sort()