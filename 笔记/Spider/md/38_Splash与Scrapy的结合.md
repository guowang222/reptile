### 安装
1. pip安装scrapy-splash库
```
 pip install scrapy-splash
```
2. scrapy-splash使用的是Splash HTTP API， 所以需要一个splash instance，一般采用docker运行splash，所以需要安装docker
3. 安装docker, 安装好后运行docker
4. 拉取镜像
```
 docker pull scrapinghub/splash
```
5. 用docker运行scrapinghub/splash
```
docker run -p 8050:8050 scrapinghub/splash
```
6. 配置splash服务（以下操作全部在settings.py）:
    1. 使用splash解析，要在配置文件中设置splash服务器地址：
    ```
    SPLASH_URL = 'http://localhost:8050/' 
    ```
    2. 将splash middleware添加到DOWNLOADER_MIDDLEWARE中
    ```
    DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    }
    ```
    3. Enable SplashDeduplicateArgsMiddleware           
    ```
    SPIDER_MIDDLEWARES = {
      'scrapy_splash.SplashDeduplicateArgsMiddleware': 100
    }
    ```
    这个中间件需要支持cache_args功能; 它允许通过不在磁盘请求队列中多次存储重复的Splash参数来节省磁盘空间。如果使用Splash 2.1+，则中间件也可以通过不将这些重复的参数多次发送到Splash服务器来节省网络流量
    
    4. 配置消息队列所使用的过滤类
    ```
    DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
    ```
    5. 配置消息队列需要使用的类
    ```
    HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
    ```
### 样例

```python
import scrapy
from scrapy_splash import SplashRequest
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    def start_requests(self):
        yield SplashRequest('https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90', args={'wait': 0.5})

    def parse(self, response):
        print(response.text)
```



