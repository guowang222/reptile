### 1. 小试牛刀
怎样扒网页呢？

其实就是根据URL来获取它的网页信息，虽然我们在浏览器中看到的是一幅幅优美的画面，但是其实是由浏览器解释才呈现出来的，实质它是一段HTML代码，加 JS、CSS，如果把网页比作一个人，那么HTML便是他的骨架，JS便是他的肌肉，CSS便是它的衣服。所以最重要的部分是存在于HTML中的，下面我们就写个例子来扒一个网页下来

```python
from urllib.request import urlopen
 
response = urlopen("http://www.baidu.com/")
print(response.read().decode())

```
真正的程序就两行，执行如下命令查看运行结果，感受一下

看，这个网页的源码已经被我们扒下来了，是不是很酸爽？



---

### 2. 常见到的方法



- requset.urlopen(url,data,timeout)
    - 第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
    
    - 第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
    
    - 第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。


- response.read()
    - read()方法就是读取文件里的全部内容，返回bytes类型
- response.getcode()
    - 返回 HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题

- response.geturl()
    - 返回 返回实际数据的实际URL，防止重定向问题

- response.info()
    - 返回 服务器响应的HTTP报头


---

### 3. Request对象
 其实上面的urlopen参数可以传入一个request请求,它其实就是一个Request类的实例，构造时需要传入Url,Data等等的内容。比如上面的两行代码，我们可以这么改写

```python

from urllib.request import urlopen
from urllib.request import Request

request = Request("http://www.baidu.com")
response = urlopen(requst)
print(response.read().decode())

```

运行结果是完全一样的，只不过中间多了一个request对象，推荐大家这么写，因为在构建请求时还需要加入好多内容，通过构建一个request，服务器响应请求得到应答，这样显得逻辑上清晰明确

---

### 4. Get 请求

大部分被传输到浏览器的html，images，js，css, … 都是通过GET方法发出请求的。它是获取数据的主要方法

例如：www.baidu.com 搜索

Get请求的参数都是在Url中体现的,如果有中文，需要转码，这时我们可使用

- urllib.parse.urlencode()

- urllib.parse. quote()



### 5. Post 请求

我们说了Request请求对象的里有data参数，它就是用在POST里的，我们要传送的数据就是这个参数data，data是一个字典，里面要匹配键值对

发送请求/响应header头的含义：

名称 | 含义
---|---
Accept | 告诉服务器，客户端支持的数据类型
Accept-Charset | 告诉服务器，客户端采用的编码
Accept-Encoding | 告诉服务器，客户机支持的数据压缩格式
Accept-Language | 告诉服务器，客户机的语言环境
Host | 客户机通过这个头告诉服务器，想访问的主机名
If-Modified-Since | 客户机通过这个头告诉服务器，资源的缓存时间
Referer | 客户机通过这个头告诉服务器，它是从哪个资源来访问服务器的。（一般用于防盗链）
User-Agent | 客户机通过这个头告诉服务器，客户机的软件环境
Cookie | 客户机通过这个头告诉服务器，可以向服务器带数据
Refresh | 服务器通过这个头，告诉浏览器隔多长时间刷新一次
Content-Type | 服务器通过这个头，回送数据的类型
Content-Language | 服务器通过这个头，告诉服务器的语言环境
Server | 服务器通过这个头，告诉浏览器服务器的类型
Content-Encoding | 服务器通过这个头，告诉浏览器数据采用的压缩格式
Content-Length | 服务器通过这个头，告诉浏览器回送数据的长度

### 6. 响应的编码
响应状态码

响应状态代码有三位数字组成，第一个数字定义了响应的类别，且有五种可能取值。
常见状态码：

号码 | 含义
-----|---
100~199 | 表示服务器成功接收部分请求，要求客户端继续提交其余请求才能完成整个处理过程
200~299 | 表示服务器成功接收请求并已完成整个处理过程。常用200（OK 请求成功）
300~399 | 为完成请求，客户需进一步细化请求。例如：请求的资源已经移动一个新地址、常用302（所请求的页面已经临时转移至新的url）、307和304（使用缓存资源）
400~499 | 客户端的请求有错误，常用404（服务器无法找到被请求的页面）、403（服务器拒绝访问，权限不够）
500~599 | 服务器端出现错误，常用500（请求未完成。服务器遇到不可预知的情况）


### 7. Ajax的请求获取数据

有些网页内容使用AJAX加载，而AJAX一般返回的是JSON,直接对AJAX地址进行post或get，就返回JSON数据了

### 8. 请求 SSL证书验证
现在随处可见 https 开头的网站，urllib可以为 HTTPS 请求验证SSL证书，就像web浏览器一样，如果网站的SSL证书是经过CA认证的，则能够正常访问，如：https://www.baidu.com/

如果SSL证书验证不通过，或者操作系统不信任服务器的安全证书，比如浏览器在访问12306网站如：https://www.12306.cn/mormhweb/的时候，会警告用户证书不受信任。（据说 12306 网站证书是自己做的，没有通过CA认证）
```
# 忽略SSL安全认证
context = ssl._create_unverified_context()
# 添加到context参数里
response = urllib.request.urlopen(request, context = context)
```