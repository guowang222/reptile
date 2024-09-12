import requests
from chaojiying_Python.chaojiying import get_code
from re import findall

login_url ='https://passport.ganji.com/login.php'
img_url = 'https://passport.ganji.com/ajax.php?dir=captcha&module=login_captcha'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
session = requests.Session()
# 打开登录页面
login_html = session.get(login_url,headers =headers)
# 提取hash
hash = findall('"__hash__":"(.+?)"',login_html.text)[0]
# 获取验证码
img_resp = session.get(img_url,headers =headers)
with open('tmp.png','wb') as f:
    f.write(img_resp.content)
# 识别图片
code = get_code('tmp.png')
# 构造登录参数
data = {
"username":"17703181473",
"password":"123456qwe",
"setcookie":"0",
"checkCode":code,
"next":"/",
"source":"passport",
"__hash__":hash,
}
# 登录
login_resp = session.post(login_url,headers = headers ,data =data)
# 打印结果
print(login_resp.text)