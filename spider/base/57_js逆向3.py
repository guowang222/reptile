import execjs
import os
os.environ["EXECJS_RUNTIME"] = "JScript"  # 环境存在才可以切换

js = ''
with open('./js_57.js','r',encoding='utf-8') as f:
    js = f.read()

ctx = execjs.compile(js)
pwd = ctx.call('get_pwd','123')
print(pwd)

# print(execjs.get().name)

# js2py