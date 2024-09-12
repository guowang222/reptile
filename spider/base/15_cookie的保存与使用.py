from urllib.request import Request,build_opener,HTTPCookieProcessor
from fake_useragent import UserAgent
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar


def get_cookie():
    url = 'https://www.kuaidaili.com/login/'
    args = {
        'username':'398707160@qq.com',
        'passwd':'123456abc'
    }
    headers = {'User-Agent':UserAgent().chrome}
    req = Request(url,headers = headers, data = urlencode(args).encode())

    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    resp = opener.open(req)
    # print(resp.read().decode())
    cookie_jar.save('cookie.txt',ignore_discard=True,ignore_expires=True)

def use_cookie():
    url = 'https://www.kuaidaili.com/usercenter/'
    headers = {'User-Agent':UserAgent().chrome}
    req = Request(url,headers = headers)
    
    cookie_jar = MozillaCookieJar()
    cookie_jar.load('cookie.txt',ignore_discard=True,ignore_expires=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    resp = opener.open(req)
    print(resp.read().decode())


if __name__ == '__main__':
    # get_cookie()
    use_cookie()