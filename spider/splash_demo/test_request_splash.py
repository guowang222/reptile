import requests

# 3个接口
def func1():
    # render.html
    url = 'https://www.lagou.com/zhaopin/Python/'
    base_url =f'http://localhost:8050/render.html?url={url}&wait=2'
    resp = requests.get(base_url)
    resp.encoding = 'utf-8'
    print(resp.text)

def func2():
    # render.png
    url = 'https://www.lagou.com/zhaopin/Python/'
    base_url =f'http://localhost:8050/render.png?url={url}&wait=2'
    resp = requests.get(base_url)
    with open('a.png','wb') as f:
        f.write(resp.content)


def func3():
    # execute
    url = 'https://www.lagou.com/zhaopin/Python/'
    lua =f'''
    function main(splash,args)
        splash:go("{url}")
        splash:wait(2)
        return splash:html()
    end
    '''
    base_url =f'http://localhost:8050/execute?lua_source={lua}'
    resp = requests.get(base_url)
    print(resp.text)

def func4():
    # 如果lua代码中有特殊字符，要通过进行quote转码
    from urllib.parse import quote
    url = 'https://www.baidu.com'
    lua =f'''
    function main(splash,args)
        splash:go("{url}")
        input = splash:select("#kw")
        input : send_text("SXT")
        splash:wait(0.1)
        button = splash:select("#su")
        button : mouse_click()
        splash : wait(2)
        return splash:html()
    end
    '''
    base_url =f'http://localhost:8050/execute?lua_source={quote(lua)}'
    resp = requests.get(base_url)
    print(resp.text)

if __name__ =='__main__':
    func4()          