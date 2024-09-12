### Selenium 调用js方法

```python
execute_script(script, *args)
```

有时候我们需要控制页面滚动条上的滚动条，但滚动条并非页面上的元素，这个时候就需要借助js是来进行操作。

一般用到操作滚动条的会两个场景：

1. 要操作的页面元素不在当前页面范围，无法进行操作，需要拖动滚动条
2. 注册时的法律条文需要阅读，判断用户是否阅读的标准是：滚动条是否拉到最下方。


#### 1.1滚动条回到顶部：

```python
js="var q=document.getElementById('id').scrollTop=0"
driver.execute_script(js)
```

#### 1.2滚动条拉到底部

```python
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
```

可以修改scrollTop 的值，来定位右侧滚动条的位置，0是最上面，10000是最底部


以上方法在Firefox和IE浏览器上上是可以的，但是用Chrome浏览器，发现不管用。Chrome浏览器解决办法：

```python
js = "var q=document.body.scrollTop=0"
driver.execute_script(js)
```

 


#### 1.3横向滚动条

```python
js = "window.scrollTo(100,400)"
driver.execute_script(js)
```

#### 1.4参考代码

```python
from selenium import webdriver
from lxml import etree
import time

url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC&pvid=845d019c94f6476ca5c4ffc24df6865a"
# 加载浏览器
wd = webdriver.Firefox()
# 发送请求
wd.get(url)
# 要执行的js
js = "var q = document.documentElement.scrollTop=10000"
# 执行js
wd.execute_script(js)

time.sleep(3)
# 解析数据
e = etree.HTML(wd.page_source)
# 提取数据的xpath
price_xpath = '//ul[@class="gl-warp clearfix"]//div[@class="p-price"]/strong/i/text()'
# 提取数据的
infos = e.xpath(price_xpath)

print(len(infos))
# 关闭浏览器
wd.quit()

```