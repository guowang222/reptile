# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class XSPipeline:
    def open_spider(self,spider):
        self.file = open('xs.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(item.get('title'))
        self.file.write('\n')
        # self.file.write(item.get('content'))
        # self.file.write('\n')
        return item
    
    def close_spider(self,spider):
        self.file.close()
