# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

class MyImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        name = item.get('img_name')
        return Request(item.get('img_url'),meta={'name':name})

    def file_path(self, request, response=None, info=None, *, item=None): # 修改图片名字
        name = request.meta.get('name')
        name = name.replace('/','_') # 处理异常字符
        return f'{name}.jpg'