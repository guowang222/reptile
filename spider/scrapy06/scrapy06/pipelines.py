# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
import pymysql
from scrapy.exceptions import DropItem

'''
1.  一个scrapy可以开启多个Pipeline
    1.1 一个pipe保存一个网站的数据
        可以通过spider来判断是否是当前网站的数据
    1.2 一个pipe保存一类数据
2. 多个Pipeline之类开启，数据传递需要写 return item
3. 当数据不想保存时，可以通DropItem进行丢弃，丢弃后，后面的Pipeline也不在处理，并且日志记录
'''

class MongoPipeline:
    def open_spider(self,spider):
        self.client = MongoClient()
        self.ssq = self.client.caipiao.ssq

    def process_item(self, item, spider):
        if item.get('code') == '2021074':
            raise DropItem('这个数据已存在')
        if spider.name =='cwl':
            return item
        else:
            self.ssq.insert_one(item)

    def close_spider(self,spider):
        self.client.close()



class MysqlPipeline:
    def open_spider(self,spider):
        self.client = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='spider',charset='utf8')
        self.cousor = self.client.cursor()

    def process_item(self, item, spider):
        if item:   
            args = [
                item.get('code'),
                item.get('red'),
                item.get('blue')
            ]
            sql = 'insert into t_ssq values (0,%s,%s,%s)'
            self.cousor.execute(sql,args)
            self.client.commit()
        return item

    def close_spider(self,spider):
        self.cousor.close()
        self.client.close()