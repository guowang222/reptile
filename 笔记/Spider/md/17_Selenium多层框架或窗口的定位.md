### 1. 窗口的定位

对于一个现代的web应用，经常会出现框架（frame） 或窗口（window）的应用，这也就给我们的定位带来了一个难题。

有时候我们定位一个元素，定位器没有问题，但一直定位不了，这时候就要检查这个元素是否在一个frame中，seelnium  webdriver 提供了一个switch_to_frame方法，可以很轻松的来解决这个问题

多层框架或窗口的定位：

- switch_to_frame()
     
**frame.html**

```html
<html>
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <title>frame</title>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
    <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css"
        rel="stylesheet" />
    <script type="text/javascript">$(document).ready(function () {
        });</script>
</head>

<body>
    <div class="row-fluid">
        <div class="span10 well">
            <h3>frame</h3><iframe id="f1" src="inner.html" width="800" , height="600"></iframe>
        </div>
    </div>
</body>
<script src="https://cdn.jsdelivr.net/npm/@bootcss/v3.bootcss.com@1.0.8/dist/js/bootstrap.min.js"></script></html>
</html>
```

**inner.html**

```html
<html>
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <title>inner</title>
</head>
<body>
    <div class="row-fluid">
        <div class="span6 well">
            <h3>inner</h3><iframe id="f2" src="http://www.baidu.com/" width="700" height="500"></iframe><a href="javascript:alert('watir-webdriver better than
    selenium webdriver;')">click</a>
        </div>
    </div>
</body>
</html>
```

#### 1.1 switch_to_frame()

```python
from selenium import webdriverimport timeimport os

browser = webdriver.Firefox()
file_path =  'file:///' + os.path.abspath('frame.html')
browser.get(file_path)

browser.implicitly_wait(30)#先找到到ifrome1（id = f1）
browser.switch_to_frame("f1")#再找到其下面的
ifrome2(id =f2)
browser.switch_to_frame("f2")

#下面就可以正常的操作元素了
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()
```