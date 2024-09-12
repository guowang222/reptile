### 1. Selenium 控制浏览器

#### 1.1  最大化窗口

我们知道调用启动的浏览器不是全屏的，这样不会影响脚本的执行，但是有时候会影响我们“观看”脚本的执行。

```python
browser = webdriver.Chrome()

url= 'http://www.baidu.com'
browser.get(url)

borwser.maximize_window()
```

#### 1.2 设置宽与高

最大化还是不够灵活，能不能随意的设置浏览的宽、高显示？当然是可以的。

```python
browser = webdriver.Chrome()

url= 'http://www.baidu.com'
browser.get(url)

borwser.set_window_size(500,600)
```
#### 1.3 浏览器前进、后退

浏览器上有一个后退、前进按钮，对于浏览网页的人是比较方便的；对于做web自动化测试的同学来说应该算是一个比较难模拟的问题；其实很简单，下面看看python的实现方式

```python
browser = webdriver.Chrome()#访问百度首页
first_url= 'http://www.baidu.com
browser.get(first_url)
time.sleep(2)#访问新闻页面
second_url='http://news.baidu.com
browser.get(second_url)
time.sleep(2)#返回（后退）到百度首页print "back to  %s "%(first_url)
browser.back()
time.sleep(1)#前进到新闻页print "forward to  %s"%(second_url)
browser.forward()
time.sleep(2)
browser.quit()
```