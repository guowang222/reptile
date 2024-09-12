from scrapy.cmdline import execute

execute('scrapy crawl save_data'.split())
# execute(['scrapy', 'crawl', 'get_data'])


# FEED_EXPORT_ENCODING ='utf-8'   如果到处的格式是json可以使用些参数
# scrapy crawl spider_name -o filename.type