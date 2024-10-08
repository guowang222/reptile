### 1. Splash介绍
> Splash是一个JavaScript渲染服务，是一个带有HTTP API的轻量级浏览器，同时它对接了Python中的Twisted和QT库。利用它，我们同样可以实现动态渲染页面的抓取

文档地址： [文档](http://splash.readthedocs.io/en/stable/)http://splash.readthedocs.io/en/stable/

### 2. 安装

#### 2.1 安装docker

[官网](https://www.docker.com/) https://www.docker.com/

[Get Started with Docker | Docker](https://www.docker.com/get-started)

https://docs.docker.com/docker-for-windows/install/

#### 2.2 拉取镜像
```
docker pull scrapinghub/splash
```
#### 2.3 用docker运行scrapinghub/splash
```
docker run -p 8050:8050 scrapinghub/splash
```
#### 2.4 查看效果
> 我们在8050端口上运行了Splash服务，打开http://192.168.99.100:8050/即可看到其Web页面
![image](https://note.youdao.com/yws/api/personal/file/366AEA0862FF4B77B584F99F058FD0FE?method=download&shareKey=1becb4e3fd74346d3e247a6cf7d8406d)

### 3 Splash对象属性
> 上图中main()方法的第一个参数是splash，这个对象非常重要，它类似于Selenium中的WebDriver对象

#### 3.1 scroll_position
> 控制页面上下或左右滚动

```
splash.scroll_position = {x=100, y=200}
```

### 4. Splash对象的方法
#### 4.1 go()
> 该方法用来请求某个链接，而且它可以模拟GET和POST请求，同时支持传入请求头、表单等数据
```
ok, reason = splash:go{url, baseurl=nil, headers=nil, http_method="GET", body=nil, formdata=nil}
```
> 返回结果是结果ok和原因reason

> 如果ok为空，代表网页加载出现了错误，此时reason变量中包含了错误的原因

参数| 含义
---|---
url | 请求的URL
baseurl | 可选参数，默认为空，表示资源加载相对路径
headers | 可选参数，默认为空，表示请求头
http_method | 可选参数，默认为GET，同时支持POST
body | 可选参数，默认为空，发POST请求时的表单数据，使用的Content-type为application/json
formdata | 可选参数，默认为空，POST的时候的表单数据，使用的Content-type为application/x-www-form-urlencoded

```
splash:go{"http://www.sxt.cn", http_method="POST", body="name=17703181473"}
```
#### 4.2 wait()

> 控制页面的等待时间
```
splash:wait{time, cancel_on_redirect=false, cancel_on_error=true}
```

参数| 含义
---|---
time | 等待的秒数
cancel_on_redirect | 可选参数，默认为false，表示如果发生了重定向就停止等待，并返回重定向结果
cancel_on_error | 可选参数，默认为false，表示如果发生了加载错误，就停止等待

```
function main(splash)
    splash:go("https://www.taobao.com")
    splash:wait(2)
    return {html=splash:html()}
end
```

#### 4.3 jsfunc()
> 直接调用JavaScript定义的方法，但是所调用的方法需要用双中括号包围，这相当于实现了JavaScript方法到Lua脚本的转换
```lua
function main(splash, args)
  splash:go("http://www.sxt.cn")
  local scroll_to = splash:jsfunc("window.scrollTo")
  scroll_to(0, 300)
  return {png=splash:png()}
end
```


```lua
function main(splash, args)
  local get_div_count = splash:jsfunc([[
  function () {
    var body = document.body;
    var divs = body.getElementsByTagName('div');
    return divs.length;
  }
  ]])
  splash:go(args.url)

  return ("There are %s DIVs in %s"):format(
    get_div_count(), args.url)
end
```



#### 4.4 evaljs()与 runjs()

- evaljs() 以执行JavaScript代码并返回最后一条JavaScript语句的返回结果
- runjs() 以执行JavaScript代码，它与evaljs()的功能类似，但是更偏向于执行某些动作或声明某些方法

```
function main(splash, args)
  splash:go("https://www.baidu.com")
  splash:runjs("foo = function() { return 'sxt' }")
  local result = splash:evaljs("foo()")
  return result
end
```

#### 4.5 html()
> 获取网页的源代码
```
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:html()
end
```
#### 4.6 png()
> 获取PNG格式的网页截图
```
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:png()
end
```
#### 4.7 har()
> 获取页面加载过程描述
```
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:har()
end
```

#### 4.8 url()
> 获取当前正在访问的URL
```
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:url()
end
```

#### 4.9 get_cookies()
> 获取当前页面的Cookies
```
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:get_cookies()
end
```
#### 4.10 add_cookie()
> 当前页面添加Cookie
```
cookies = splash:add_cookie{name, value, path=nil, domain=nil, expires=nil, httpOnly=nil, secure=nil}
```

```
function main(splash)
    splash:add_cookie{"sessionid", "123456abcdef", "/", domain="http://bjsxt.com"}
    splash:go("http://bjsxt.com/")
    return splash:html()
end
```
#### 4.11 clear_cookies()
> 可以清除所有的Cookies
```
function main(splash)
    splash:go("https://www.bjsxt.com/")
    splash:clear_cookies()
    return splash:get_cookies()
end
```
#### 4.12 set_user_agent()
> 设置浏览器的User-Agent
```
function main(splash)
  splash:set_user_agent('Splash')
  splash:go("http://httpbin.org/get")
  return splash:html()
end
```
#### 4.13 set_custom_headers()
> 设置请求头
```
function main(splash)
  splash:set_custom_headers({
     ["User-Agent"] = "Splash",
     ["Site"] = "Splash",
  })
  splash:go("http://httpbin.org/get")
  return splash:html()
end
```

#### 4.14 select()
> 选中符合条件的第一个节点

> 如果有多个节点符合条件，则只会返回一个

> 其参数是CSS选择器
```
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  splash:wait(3)
  return splash:png()
end
```

#### 4.15 send_text()
> 填写文本
```
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  splash:wait(3)
  return splash:png()
end
```
#### 4.16 mouse_click()
> 模拟鼠标点击操作
```
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  submit = splash:select('#su')
  submit:mouse_click()
  splash:wait(3)
  return splash:png()
end
```
#### 4.17 代理Ip
```
function main(splash)
    splash:on_request(function(request)
        request:set_proxy{
            host='61.138.33.20',
            port=808,
            username='uanme',
            password='passwrod'
        }
    
     end)
    
    -- 设置请求头
    splash:set_user_agent("Mozilla/5.0")

    splash:go("https://httpbin.org/get")
    return splash:html()
end
```

### 5 Splash与Python结合
#### 5.1 render.html
> 此接口用于获取JavaScript渲染的页面的HTML代码，接口地址就是Splash的运行地址加此接口名称，例如`http://192.168.99.100:8050/render.html`

```
import requests
url = 'http://192.168.99.100:8050/render.html?url=https://www.bjsxt.com&wait=3'
response = requests.get(url)
print(response.text)
```
#### 5.2 render.png
> 此接口可以获取网页截图
```
import requests
 
url = 'http://192.168.99.100:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('taobao.png', 'wb') as f:
    f.write(response.content)
```

#### 5.3 execute
> 最为强大的接口。前面说了很多Splash Lua脚本的操作，用此接口便可实现与Lua脚本的对接

```
import requests
from urllib.parse import quote
 
lua = '''
function main(splash)
    return 'hello'
end
'''
 
url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
```