import json

str_ = '{"name":"战狼3"}'
print(type(str_))
print('str 2 obj')
obj = json.loads(str_)
print(str_)
print(obj)
print(type(obj))

print('obj 2 str')
str2 = json.dumps(obj,ensure_ascii=False)
print(type(str2))
print(str2)

print('obj 2 file')

json.dump(obj,open('movie.txt','w',encoding='utf-8'))

print('file 2 obj')
obj2 = json.load(open('movie.txt',encoding='utf-8'))
print(obj2)
print(type(obj2))

