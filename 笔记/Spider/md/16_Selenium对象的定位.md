对象的定位应该是自动化的核心，要想操作一个对象，首先应该识别这个对象。
一个对象就是一个人一样，他会有各种的特征（属性），如比我们可以通过一个人的身份证号，姓名，或者他住在哪个街道、楼层、门牌找到这个人。

#### 1.1 对象定位 

webdriver提供了一系列的对象定位方法，常用的有以下几种

单个元素选取
- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

多个元素选取
- find_elements_by_name
- find_elements_by_xpath
- find_elements_by_link_text
- find_elements_by_partial_link_text
- find_elements_by_tag_name
- find_elements_by_class_name
- find_elements_by_css_selector

利用 By 类来确定哪种选择方式
```shell
from selenium.webdriver.common.by import By
```
By 类的一些属性如下
- ID = "id"
- XPATH = "xpath"
- LINK_TEXT = "link text"
- PARTIAL_LINK_TEXT = "partial link text"
- NAME = "name"
- TAG_NAME = "tag name"
- CLASS_NAME = "class name"
- CSS_SELECTOR = "css selector"

我们可以看到，一个百度的输入框，可以用这么用种方式去定位

```python
browser = webdriver.chrome()

browser.get("http://www.baidu.com")
time.sleep(2)
#########百度输入框的定位方式##########
#通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")
#通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")
#通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys("selenium")
#通过class name 方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
#通过CSS方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
#通过xphan方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
############################################
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()
```

#### 1.2 层级定位
假如两个控件，他们长的一模样，还都叫“张三”，唯一的不同是一个在北京，一个在上海，那我们就可以通过，他们的城市，区，街道，来找到他们。

在实际的开发中也经常会遇到这种问题：页面上有很多个属性基本相同的元素，现在需要具体定位到其中的一个。由于属性基本相当，所以在定位的时候会有些麻烦，这时候就需要用到层级定位。先定位父元素，然后再通过父元素定位子孙元素

```html
<html>
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        <title>Level Locate</title>        
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/@bootcss/v3.bootcss.com@1.0.9/dist/css/bootstrap.min.css" rel="stylesheet" />        
    </head>
    <body>
        <h3>Level locate</h3>
        <div class="span3 col-md-3">        
            <div class="well">
                <div class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">Link1</a>
                    <ul class="dropdown-menu" role="menu" aria-labelledby="dLabel" id="dropdown1" >
                        <li><a tabindex="-1" href="http://www.bjsxt.com">Action</a></li>
                        <li><a tabindex="-1" href="#">Another action</a></li>
                        <li><a tabindex="-1" href="#">Something else here</a></li>
                        <li class="divider"></li>
                        <li><a tabindex="-1" href="#">Separated link</a></li>
                    </ul>
                </div>                
            </div>            
        </div>
        <div class="span3 col-md-3">        
            <div class="well">
                <div class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">Link2</a>
                    <ul class="dropdown-menu" role="menu" aria-labelledby="dLabel" >
                        <li><a tabindex="-1" href="#">Action</a></li>
                        <li><a tabindex="-1" href="#">Another action</a></li>
                        <li><a tabindex="-1" href="#">Something else here</a></li>
                        <li class="divider"></li>
                        <li><a tabindex="-1" href="#">Separated link</a></li>
                    </ul>
                </div>                
            </div>            
        </div>
    </body>
    <script src="https://cdn.jsdelivr.net/npm/@bootcss/v3.bootcss.com@1.0.9/dist/js/bootstrap.min.js"></script></html>
```

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

chrome = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('level_locate.html')
chrome.get(file_path)
#点击Link1链接（弹出下拉列表)
chrome.find_element_by_link_text('Link1').click()
#找到id 为dropdown1的父元素
WebDriverWait(chrome, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
#在父亲元件下找到link为Action的子元素
menu = chrome.find_element_by_id('dropdown1').find_element_by_link_text('Action')
#鼠标定位到子元素上
webdriver.ActionChains(chrome).move_to_element(menu).perform()

time.sleep(2)
chrome.quit()
```

具体思路是：先点击显示出1个下拉菜单，然后再定位到该下拉菜单所在的ul，再定位这个ul下的某个具体的link。在这里，我们定位第1个下拉菜单中的Action这个选项。

虽然我每行代码前叫了注释，但可能还是不太容易理解，因为里面多了不少以前没见过的新东东。

WebDriverWait(chrome, 10) 

10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束。chrome.Chrome()的句柄
就不解释了，前面操作webdriver.Chrome()的句柄


#### 1.3 操作元素
前面讲到了不少知识都是定位元素，定位只是第一步，定位之后需要对这个原素进行操作。

鼠标点击呢还是键盘输入，这要取决于我们定位的是按钮还输入框。

一般来说，webdriver中比较常用的操作对象的方法有下面几个

- click 点击对象
- send_keys 在对象上模拟按键输入
- clear 清除对象的内容，如果可以的话

```python
browser = webdriver.Chrome()

browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").clear()
browser.find_element_by_id("kw").send_keys("itbaizhan")
browser.find_element_by_id("su").click()
driver.find_element_by_id("user_pwd").send_keys(Keys.ENTER)
browser.quit()
```
