### Scrapy内置设置

[settings-2.5.0文档 (scrapy.org)](https://docs.scrapy.org/en/latest/topics/settings.html#topics-settings-ref)

下面给出scrapy提供的常用内置设置列表,你可以在settings.py文件里面修改这些设置，以应用或者禁用这些设置项

- BOT_NAME

    默认: 'scrapybot'
    
    Scrapy项目实现的bot的名字。用来构造默认 User-Agent，同时也用来log。
    当你使用 startproject 命令创建项目时其也被自动赋值。
    
- CONCURRENT_ITEMS

    默认: 100
    
    Item Processor(即 Item Pipeline) 同时处理(每个response的)item的最大值
    
- CONCURRENT_REQUESTS

    默认: 16

    Scrapy downloader 并发请求(concurrent requests)的最大值。
    
- CONCURRENT_REQUESTS_PER_DOMAIN

    默认: 8
    
    对单个网站进行并发请求的最大值。
    
- CONCURRENT_REQUESTS_PER_IP

    默认: 0

    对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定， 使用该设定。 也就是说，并发限制将针对IP，而不是网站。
    
    该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0，下载延迟应用在IP而不是网站上。
    
- FEED_EXPORT_ENCODING ='utf-8' 

    设置导出时文件的编码

- DEFAULT_REQUEST_HEADERS

    默认:
    ```python
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
    }
    ```
    Scrapy HTTP Request使用的默认header。由 DefaultHeadersMiddleware 产生。
    
- DOWNLOADER

    默认: 'scrapy.core.downloader.Downloader'
    
    用于crawl的downloader.
    
- DOWNLOADER_MIDDLEWARES

    默认:: {}
    
    保存项目中启用的下载中间件及其顺序的字典
    
- DOWNLOAD_DELAY

    默认: 0
    
    下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数
    
- DOWNLOAD_TIMEOUT

    默认: 180
    
    下载器超时时间(单位: 秒)
    
- ITEM_PIPELINES

    默认: {}

    保存项目中启用的pipeline及其顺序的字典。该字典默认为空，值(value)任意。 不过值(value)习惯设定在0-1000范围内
    
- DEPTH_LIMIT

    默认：`0`

    类：`scrapy.spidermiddlewares.depth.DepthMiddleware`

    允许为任何站点爬行的最大深度。如果为零，则不会施加任何限制。

- LOG_ENABLED

    默认: True

    是否启用logging
    
- LOG_ENCODING

    默认: 'utf-8'
    
    logging使用的编码。
    
- LOG_FILE

    默认: None

    logging输出的文件名。如果为None，则使用标准错误输出(standard error)。
    
- LOG_FORMAT

    默认: '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

    日志的数据格式
    
- LOG_DATEFORMAT

    默认: '%Y-%m-%d %H:%M:%S'

    日志的日期格式
    
- LOG_LEVEL

    默认: 'DEBUG'
    
    log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG
    
- LOG_STDOUT

    默认: False

    如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中
    
- RANDOMIZE_DOWNLOAD_DELAY

    默认: True
    
    如果启用，当从相同的网站获取数据时，Scrapy将会等待一个随机的值 (0.5到1.5之间的一个随机值 * DOWNLOAD_DELAY)
    
    该随机值降低了crawler被检测到(接着被block)的机会。某些网站会分析请求， 查找请求之间时间的相似性
    
- REDIRECT_MAX_TIMES

    默认: 20

    定义request允许重定向的最大次数。超过该限制后该request直接返回获取到的结果。 对某些任务我们使用Firefox默认值
    
- ROBOTSTXT_OBEY

    默认: True

    是否遵循robots协议
    
- USER_AGENT

    默认: "Scrapy/VERSION (+http://scrapy.org)"
    
    爬取的默认User-Agent，除非被覆盖
#### Scrapy默认BASE设置
> scrapy对某些内部组件进行了默认设置，这些组件通常情况下是不能被修改的，但是我们在自定义了某些组件以后，比如我们设置了自定义的middleware中间件，需要按照一定的顺序把他添加到组件之中，这个时候需要参考scrapy的默认设置，因为这个顺序会影响scrapy的执行，下面列出了scrapy的默认基础设置

注意：如果你想要修改以下的某些设置，应该避免直接修改下列内容，而是修改其对应的自定义内容，例如，你想修改下面的`DOWNLOADER_MIDDLEWARES_BASE`的内容，你应该去修改`DOWNLOADER_MIDDLEWARES`这个内容，只是去掉了_BASE而已，其他的也是类似这样

- DOWNLOADER_MIDDLEWARES_BASE

默认:

```python
{
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 500,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 550,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
}
```
包含Scrapy默认启用的下载中间件的字典。 永远不要在项目中修改该设定，而是修改 DOWNLOADER_MIDDLEWARES 。

- SPIDER_MIDDLEWARES_BASE

默认:

```python
{
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
}
```
保存项目中默认启用的spider中间件的字典。 永远不要在项目中修改该设定，而是修改 SPIDER_MIDDLEWARES 。
EXTENSIONS_BASE

默认:
```python
{
    'scrapy.extensions.corestats.CoreStats': 0,
    'scrapy.telnet.TelnetConsole': 0,
    'scrapy.extensions.memusage.MemoryUsage': 0,
    'scrapy.extensions.memdebug.MemoryDebugger': 0,
    'scrapy.extensions.closespider.CloseSpider': 0,
    'scrapy.extensions.feedexport.FeedExporter': 0,
    'scrapy.extensions.logstats.LogStats': 0,
    'scrapy.extensions.spiderstate.SpiderState': 0,
    'scrapy.extensions.throttle.AutoThrottle': 0,
}
```
可用的插件列表。需要注意，有些插件需要通过设定来启用。默认情况下， 该设定包含所有稳定(stable)的内置插件。
- DOWNLOAD_HANDLERS_BASE

默认:
```python
{
    'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
    'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
    'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
    's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
}
```
保存项目中默认启用的下载处理器(request downloader handler)的字典。 永远不要在项目中修改该设定，而是修改 DOWNLOADER_HANDLERS 。

如果需要关闭上面的下载处理器，您必须在项目中的 DOWNLOAD_HANDLERS 设定中设置该处理器，并为其赋值为 None 。

**说明**

即使我们添加了一些我们自定义的组件，scrapy默认的base设置依然会被应用，这样说可能会一头雾水，简单地例子：

假如我们在middlewares.py文件中定义了一个中间件，名称为MyMiddleware，我们把它添加到settings.py文件里面的`DOWNLOADER_MIDDLEWARES`，且他的执行顺序我们设置为450，最终的设置内容就是：
```python
DOWNLOADER_MIDDLEWARES = {
    'cnblog.middlewares.MyMiddleware':450,
}
```
我们再来看一下默认的`DOWNLOADER_MIDDLEWARES_BASE`的内容：
```python
DOWNLOADER_MIDDLEWARES_BASE ={
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 500,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 550,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
}
```
这个时候，scrapy下载中间件的最终的执行顺序就是，把`DOWNLOADER_MIDDLEWARES`和`DOWNLOADER_MIDDLEWARES_BASE`里面的中间件按照顺序执行，`100>300>350>400>450>500>550>580>590>600>700>750>830>850>900`且全部执行，并不会因为我们定义了一个中间件，而使默认的中间件失效，也就是说，最终的结果其实是合并执行。

如果我们不想应用某一个默认的中间件，假如`'scrapy.downloadermiddlewares.retry.RetryMiddleware': 500,`那么，就应该在`DOWNLOADER_MIDDLEWARES`里面把它的值设置为None，像下面这样：
```python
DOWNLOADER_MIDDLEWARES = {
    'cnblog.middlewares.MyMiddleware':450,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware':None，
}
```
