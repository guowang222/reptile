### 1. Selenium 安装与测试

Selenium是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，类型像我们玩游戏用的按键精灵，可以按指定的命令自动操作，不同是Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器）。

Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。

Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器。

PyPI网站下载 Selenium库 https://pypi.python.org/simple/selenium ，也可以用 第三方管理器 

pip用命令安装：`pip install selenium`

Selenium 官方参考文档：http://selenium-python.readthedocs.io/index.html


#### 1.1 安装Firefox geckodriver
安装firefox最新版本，添加Firefox可执行程序到系统环境变量。记得关闭firefox的自动更新

firefox下载地下：https://github.com/mozilla/geckodriver/releases

将下载的geckodriver.exe 放到path路径下 D:\Python\python_version\

#### 1.2 安装ChromeDriver
http://chromedriver.storage.googleapis.com/index.html
> 注意版本号要对应

> 下载下来的文件解压到`python_version\Scripts`

**测试代码**
```python
# 导入 webdriver
from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.Chrome()
# 如果没有在环境变量指定PhantomJS位置
# driver = webdriver.Chrome(executable_path="./phantomjs"))
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com/")
# 打印网页渲染后的源代码
print(driver.page_source)
# 获取当前页面Cookie
print(driver.get_cookies())
# 生成新的页面快照
driver.save_screenshot("python爬虫.png")
# 获取当前url
print(driver.current_url)
# 关闭浏览器
driver.quit()
# 浏览器退出Bug-解决方案
os.system('taskkill /im chromedriver.exe /F')
os.system('taskkill /im chrome.exe /F')
```
