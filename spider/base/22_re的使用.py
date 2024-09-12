import re

str ='I study python3.9 every_day'
print('------------------match(规则，从哪个字符串匹配)-----------------------') # 从头开始匹配，如果有地匹配不上，就不会返回数据None
m1 = re.match(r'I',str)
m2 = re.match(r'\w',str)
m3 = re.match(r'\S',str)
m4 = re.match(r'\D',str)
m5 = re.match(r'I (study)',str)
m6 = re.match(r'I (s\w*)',str)
m6 = re.match(r'I (s\w*?)',str)
print(m6.group(1)) # group是在能匹配到对象的时候使用

print('------------------search(规则，从哪个字符串匹配)-----------------------') # 从任意位置开始匹配，匹配第一个数据
s1 = re.search(r'\D',str)
s2 = re.search(r's\w+',str)
s3 = re.search(r'y',str)
s4 = re.search(r'p\w+',str)
s5 = re.search(r'p\w+.\d',str)
print(s5.group())

print('------------------findall(规则，从哪个字符串匹配)-----------------------')# 从任意位置开始匹配，匹配所有数据
f1 = re.findall(r'eva',str)
print(f1)

print('------------------sub(匹配表达式,替换成什么样,原字符串)-----------------------')
su1 = re.sub('python','Python',str)
su2 = re.sub('e\w+','Every_day',str)
print(su2)
# print(str)

print('------------------test()-----------------------')
html = '<div><a class="title" href="http://www.bjsxt.com">尚学堂</a></div>'

t1 = re.findall(r'<a class="title" href="http://www.bjsxt.com">([\u4e00-\u9fa5]+)</a>',html)
t2 = re.findall(r'<a class="title" href="(.+)">[\u4e00-\u9fa5]+</a>',html)
t3 = re.findall(r'<a class="title" href="(.+)">(.+)</a>',html)
print(t3)