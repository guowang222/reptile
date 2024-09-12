import requests

def login_input():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    session = requests.Session()

    login_url ='http://www.chaojiying.com/user/login/'
    img_url = 'http://www.chaojiying.com/include/code/code.php?u=1'

    img_resp = session.get(img_url,headers =headers)
    with open('tmp.png','wb') as f:
        f.write(img_resp.content)

    code = input('请输入验证码：')
    params = {
    'user': 'feelingslw',
    'pass': '123456',
    'imgtxt': code,
    'act': '1'
    }

    resp = session.post(login_url,data=params, headers=headers)
    print(resp.text)

def login_auto():  
    from chaojiying_Python.chaojiying import get_code  
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    session = requests.Session()

    login_url ='http://www.chaojiying.com/user/login/'
    img_url = 'http://www.chaojiying.com/include/code/code.php?u=1'

    img_resp = session.get(img_url,headers =headers)
    with open('tmp.png','wb') as f:
        f.write(img_resp.content)

    code = get_code('tmp.png')
    params = {
    'user': 'feelingslw',
    'pass': '123456',
    'imgtxt': code,
    'act': '1'
    }

    resp = session.post(login_url,data=params, headers=headers)
    print(resp.text)

if __name__ == "__main__":
    login_auto()