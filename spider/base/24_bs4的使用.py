# pip install bs4
# pip install lxml

from bs4 import BeautifulSoup

html = '''
<title id="title">尚学堂</title>
<div class="info" float="left">Welcome to BaiZhan</div>
<div class="info" float="right">
    <span>Good Good Study</span>
    <a href="www.bjsxt.com"></a>
    <strong><!-- 这个是注释啊 --></strong>
</div>
'''
soup = BeautifulSoup(html,'lxml')
print('-------------------获取标签------------------------')    # 只会获取第一个标签，不用考虑层级关系
print(soup.title)
print(soup.div)
print(soup.span)
print('-------------------获取属性------------------------')
print(soup.div.attrs)
print(soup.div.get('class'))
print(soup.div['float'])
print(soup.a.get('href'))
print('-------------------获取内容------------------------')
print(soup.title.string)
print(soup.title.text)
print(type(soup.title.string))
print(type(soup.title.text))
print('-------------------获取内容注释------------------------')
print(soup.strong.string)
print(soup.strong.text)
print(type(soup.strong.string))
print(type(soup.strong.text))
print(soup.strong.prettify())

print('-------------------find_all()------------------------')
print(soup.find_all('div'))
print(soup.find_all(id='title'))
print(soup.find_all(class_='info'))
print(soup.find_all(attrs={'float':'right'}))
print(soup.find_all('div',attrs={'float':'left'}))

print('-------------------css选择器()------------------------') # 也是获取多个内容
print(soup.select('div'))
print(soup.select('#title'))
print(soup.select('.info'))
print(soup.select('div > span'))
print(soup.select('div.info > a'))
'''
#beautiful-soup-4-4-0 > h1
'''