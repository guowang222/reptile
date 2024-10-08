### 1. pyquery
#### 1.1 介绍
> 如果你对CSS选择器与Jquery有有所了解，那么还有个解析库可以适合你--Jquery

> [官网](https://pythonhosted.org/pyquery/)https://pythonhosted.org/pyquery/
#### 1.2 安装
> pip install pyquery
#### 1.3 使用方式
##### 1.3.1 初始化方式
- 字符串
```python
    from pyquery import PyQuery as pq
    doc = pq(str)
    print(doc(tagname))
```
- url
```python
    from pyquery import PyQuery as pq
    doc = pq(url='http://www.baidu.com')
    print(doc('title'))
```
- 文件
```python
    from pyquery import PyQuery as pq
    doc = pq(filename='demo.html')
    print(doc(tagname))
```

##### 1.3.2 选择节点
- 获取当前节点
```python
    from pyquery import PyQuery as pq
    doc = pq(filename='demo.html')
    doc('#main #top')
```
- 获取子节点
    - 在doc中一层层写出来
    - 获取到父标签后使用children方法
```python
    from pyquery import PyQuery as pq
    doc = pq(filename='demo.html')
    doc('#main #top').children()
    
```
- 获取父节点
    - 获取到当前节点后使用parent方法
- 获取兄弟节点
    - 获取到当前节点后使用siblings方法
##### 1.3.3 获取属性
```python
    from pyquery import PyQuery as pq
    doc = pq(filename='demo.html')
    a = doc('#main #top')
    print(a.attrib['href'])  #Element
    print(a.attr('href')) #PyQuery
```
##### 1.3.4 获取内容
```python
    from pyquery import PyQuery as pq
    doc = pq(filename='demo.html')
    div = doc('#main #top')
    print(a.html())
    print(a.text()) # pyquery
    print(a.text) #element
```

##### 1.3.5 样例
```python

from pyquery import PyQuery as pq
# 1.可加载一段HTML字符串，或一个HTML文件，或是一个url地址，
d=pq("<html><title>hello</title></html>")
d=pq(filename=path_to_html_file)
d=pq(url='http://www.baidu.com')注意：此处url似乎必须写全
 
# 2.html()和text() ——获取相应的HTML块或文本块，
p=pq("<head><title>hello</title></head>")
p('head').html()#返回<title>hello</title>
p('head').text()#返回hello
 
# 3.根据HTML标签来获取元素，
d=pq('<div><p>test 1</p><p>test 2</p></div>')
d('p')#返回[<p>,<p>]
print d('p')#返回<p>test 1</p><p>test 2</p>
print d('p').html()#返回test 1
# 注意：当获取到的元素不只一个时，html()方法只返回首个元素的相应内容块
 
# 4.eq(index) ——根据给定的索引号得到指定元素。接上例，若想得到第二个p标签内的内容，则可以：
print d('p').eq(1).html() #返回test 2
 
# 5.filter() ——根据类名、id名得到指定元素，例：
d=pq("<div><p id='1'>test 1</p><p class='2'>test 2</p></div>")
d('p').filter('#1') #返回[<p#1>]
d('p').filter('.2') #返回[<p.2>]
 
# 6.find() ——查找嵌套元素，例：
d=pq("<div><p id='1'>test 1</p><p class='2'>test 2</p></div>")
d('div').find('p')#返回[<p#1>, <p.2>]
d('div').find('p').eq(0)#返回[<p#1>]
 
#7.直接根据类名、id名获取元素，例：
d=pq("<div><p id='1'>test 1</p><p class='2'>test 2</p></div>")
d('#1').html()#返回test 1
d('.2').html()#返回test 2
 
# 8.获取属性值，例：
d=pq("<p id='my_id'><a href='http://hello.com'>hello</a></p>")
d('a').attr('href')#返回http://hello.com
d('p').attr('id')#返回my_id
 
# 9.修改属性值，例：
d('a').attr('href', 'http://baidu.com')把href属性修改为了baidu
 
# 10.addClass(value) ——为元素添加类，例：
d=pq('<div></div>')
d.addClass('my_class')#返回[<div.my_class>]
 
# 11.hasClass(name) #返回判断元素是否包含给定的类，例：
d=pq("<div class='my_class'></div>")
d.hasClass('my_class')#返回True
 
# 12.children(selector=None) ——获取子元素，例：
d=pq("<span><p id='1'>hello</p><p id='2'>world</p></span>")
d.children()#返回[<p#1>, <p#2>]
d.children('#2')#返回[<p#2>]
 
# 13.parents(selector=None)——获取父元素，例：
d=pq("<span><p id='1'>hello</p><p id='2'>world</p></span>")
d('p').parents()#返回[<span>]
d('#1').parents('span')#返回[<span>]
d('#1').parents('p')#返回[]
 
# 14.clone() ——返回一个节点的拷贝
 
#15.empty() ——移除节点内容
 
# 16.nextAll(selector=None) ——返回后面全部的元素块，例：
d=pq("<p id='1'>hello</p><p id='2'>world</p><img scr='' />")
d('p:first').nextAll()#返回[<p#2>, <img>]
d('p:last').nextAll()#返回[<img>]
 
# 17.not_(selector) ——返回不匹配选择器的元素，例：
d=pq("<p id='1'>test 1</p><p id='2'>test 2</p>")
d('p').not_('#2')#返回[<p#1>]
```