### selenium参数的使用

#### 1 元素拖拽
> 要完成元素的拖拽，首先你需要指定被拖动的元素和拖动目标元素，然后利用 ActionChains 类来实现

```html
<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>jQuery UI Draggable - Auto-scroll</title>
	<link rel="stylesheet" href="http://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
	<style>
	#draggable, #draggable2, #draggable3 { width: 100px; height: 100px; padding: 0.5em; float: left; margin: 0 10px 10px 0; }
    body {font-family: Arial, Helvetica, sans-serif;}
    table {font-size: 1em;}
    .ui-draggable, .ui-droppable {background-position: top;}
	</style>
	<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
	<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
	<script>
	$( function() {
		$( "#draggable" ).draggable({ scroll: true });
		$( "#draggable2" ).draggable({ scroll: true, scrollSensitivity: 100 });
		$( "#draggable3" ).draggable({ scroll: true, scrollSpeed: 100 });
	} );
	</script>
</head>
<body>
<div id="draggable" class="ui-widget-content">
	<p>Scroll set to true, default settings</p>
</div>

<div id="draggable2" class="ui-widget-content">
	<p>scrollSensitivity set to 100</p>
</div>

<div id="draggable3" class="ui-widget-content">
	<p>scrollSpeed set to 100</p>
</div>
<div style="height: 5000px; width: 1px;"></div>
</body>
</html>

```

以下实现元素从 source 拖动到 target 的操作
```python
import os
chrome.get(f'file:///{os.path.abspath("./html/scroll.html")}')

div1 = chrome.find_element_by_id('draggable')
div2 = chrome.find_element_by_id('draggable2')
div3 = chrome.find_element_by_id('draggable3')

from selenium.webdriver import ActionChains
from time import sleep

sleep(2)
action_chains = ActionChains(chrome)
# 将页面上的第一个能被拖拽的元素拖拽到第二个元素位置 
action_chains.drag_and_drop(div1, div2).perform()

# 将页面上的第三个能拖拽的元素，向右下拖动10个像素，共拖动5次
a = action_chains.drag_and_drop_by_offset(div3, 10, 10)
for i in range(5):
    a.perform()
    sleep(2) 
```

#### 2. 参数的使用
> chrome59版本以后可以变成无头的浏览器，加以下参数
```python
options = webdriver.ChromeOptions()
options.add_argument('--headless')
chrome = webdriver.Chrome(chrome_options=options)
chrome.get("http://www.baidu.com")
```

> 代理模式
```python
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("--proxy-server=http://61.138.33.20:808")
chrome = webdriver.Chrome(chrome_options=option)
chrome.get('http://httpbin.org/get')
info = chrome.page_source

print(info)

```
> 防检测设置

```python
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

options.add_experimental_option('useAutomationExtension', False)
chrome = webdriver.Chrome(chrome_options=option)
chrome.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})

chrome.get('http://httpbin.org/get')
info = chrome.page_source

print(info)
```

> 使用 `window.navigator.webdriver` 检测
