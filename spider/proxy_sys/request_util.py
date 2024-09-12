import requests
from lxml import etree
from config import logging

class WebRequest:
    '''
    专门发送请求使用
    '''
    def __init__(self):
        self.resp = None
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

    def do_get(self,url,headers = None,*arg,**kwargs):
        '''
        get请求
        headers若传递了就使用传递的headers
        若没传递就使用默认的headers
        '''
        try:
            if not headers:
                headers = self.headers
            resp = requests.get(url,headers = headers,*arg,**kwargs)
            if resp.status_code == 200:
                resp.encoding ='utf-8'
                self.resp = resp
                return resp
        except Exception as e:
            logging.info(e)

    def do_post(self,url,headers = None,*arg,**kwargs):
        try:
            if not headers:
                headers = self.headers
            resp = requests.post(url,headers = headers,*arg,**kwargs)
            if resp.status_code == 200:
                resp.encoding ='utf-8'
                self.resp = resp
                return resp
        except Exception as e:
            logging.info(e)
    
    def get_tree(self):
        e = etree.HTML(self.resp.text)
        return e
    
    def get_text(self):
        return self.resp.text
    
    def get_json(self):
        return self.resp.json()
    
    def get_content(self):
        return self.resp.content