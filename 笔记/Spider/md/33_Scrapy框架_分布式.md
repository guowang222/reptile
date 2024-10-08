### 1. 介绍scrapy-redis框架
scrapy-redis
> 一个三方的基于redis的分布式爬虫框架，配合scrapy使用，让爬虫具有了分布式爬取的功能。

github地址：
https://github.com/darkrho/scrapy-redis

### 2. 分布式原理

![image-20210706131816615](../img/image-20210706131816615.png)

　scrapy-redis实现分布式，其实从原理上来说很简单，这里为描述方便，我们把自己的**核心服务器**称为**master**，而把用于**跑爬虫程序**的机器称为**slave**

我们知道，采用scrapy框架抓取网页，我们需要首先给定它一些start_urls，爬虫首先访问start_urls里面的url，再根据我们的具体逻辑，对里面的元素、或者是其他的二级、三级页面进行抓取。而要实现分布式，我们只需要在这个starts_urls里面做文章就行了

我们在**master**上搭建一个**redis数据库**`（注意这个数据库只用作url的存储)，并对每一个需要爬取的网站类型，都开辟一个单独的列表字段。通过设置slave上scrapy-redis获取url的地址为master地址。这样的结果就是，**尽管有多个slave，然而大家获取url的地方只有一个，那就是服务器master上的redis数据库**

并且，由于scrapy-redis**自身的队列机制**，slave获取的链接不会相互冲突。这样各个slave在完成抓取任务之后，再把获取的结果汇总到服务器上

**好处**

程序移植性强，只要处理好路径问题，把slave上的程序移植到另一台机器上运行，基本上就是复制粘贴的事情

### 3.分布式爬虫的实现
1. 使用三台机器，一台是win10，两台是centos，分别在两台机器上部署scrapy来进行分布式抓取一个网站

2. win10的ip地址为`192.168.31.245`，用来作为redis的master端，centos的机器作为slave

3. master的爬虫运行时会把提取到的url封装成request放到redis中的数据库：“dmoz:requests”，并且从该数据库中提取request后下载网页，再把网页的内容存放到redis的另一个数据库中“dmoz:items”

4. slave从master的redis中取出待抓取的request，下载完网页之后就把网页的内容发送回master的redis

5. 重复上面的3和4，直到master的redis中的“dmoz:requests”数据库为空，再把master的redis中的“dmoz:items”数据库写入到mongodb中

6. master里的reids还有一个数据“dmoz:dupefilter”是用来存储抓取过的url的指纹（使用哈希函数将url运算后的结果），是防止重复抓取的

### 4. scrapy-redis框架的安装

![image-20210706124606382](../img/image-20210706124606382.png)

```python
pip install scrapy-redis
```

### 5. 部署scrapy-redis

#### 5.1 slave端
> 在windows上的settings.py文件的最后增加如下一行
```python
REDIS_HOST = 'localhost' #master IP

REDIS_PORT = 6379
```

配置好了远程的redis地址后启动两个爬虫（启动爬虫没有顺序限制）
#### 6 给爬虫增加配置信息

```python
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
```

#### 7 运行程序
##### 7.1 运行slave
```python
scrapy runspider 文件名.py
```
开起没有先后顺序

##### 7.2 运行master
```python
lpush (redis_key)  url #括号不用写
```
**说明**
- 这个命令是在redis-cli中运行
- redis_key 是 spider.py文件中的redis_key的值
- url 开始爬取地址，不加双引号


#### 8 数据导入到mongodb中

等到爬虫结束后,如果要把数据存储到mongodb中，就应该修改master端process_items.py文件，如下

```python
import redis
import pymongo

def main():
    r = redis.Redis(host='192.168.31.245',port=6379,db=0)
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.dmoz
    sheet = db.sheet
    
    while True:
        source, data = r.blpop(["dmoz:items"])
        item = json.loads(data)
        sheet.insert(item)

if __name__ == '__main__':
    main()
```
#### 9 数据导入到MySQL中

等到爬虫结束后,如果要把数据存储到mongodb中，就应该修改master端process_items.py文件，如下

```python
import redis
import pymysql
import json
def process_item():
    r_client = redis.Redis(host="127.0.0.1",port=6379,db =0)
    m_client = pymysql.connect(host="127.0.0.1",port=3306,user="root",passowrd="123456",db="lianjia")
    source,data =r_client.blpop("lianjia:item")
    item = json.loads(data)

    cursor = m_client.cursor()
    values = []
    cursor.execute(sql,values)
```