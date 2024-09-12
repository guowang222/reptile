# pip install requests
import requests

def no_args():
    url = 'http://www.sxt.cn/'
    resp = requests.get(url)
    print(resp.text)
def use_args():
    url = 'http://www.baidu.com/s'
    args = {
        'wd':'尚学堂'
    }
    resp = requests.get(url,params=args)
    print(resp.text)

if __name__ == '__main__':
    use_args()