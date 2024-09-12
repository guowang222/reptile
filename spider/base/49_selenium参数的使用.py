from selenium import webdriver

def headless():
    # 设置成无头浏览器
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe',options = options)
    chrome.get('http://www.baidu.com/')
    print(chrome.page_source)
    chrome.quit()

def proxy():
    # 设置代理
    options = webdriver.ChromeOptions()
    # options.add_argument('--proxy-server=type://ip:port')
    options.add_argument('--proxy-server=http://113.238.142.208:3128')

    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe',options = options)
    chrome.get('http://httpbin.org/get')
    print(chrome.page_source)
    chrome.quit()

def jiance():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    chrome = webdriver.Chrome(executable_path='./tools/chromedriver.exe')

    chrome.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
      "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => false
        })
      """
    })


    chrome.get('http://www.baidu.com/')
    print(chrome.page_source)
    chrome.quit()

# if __name__ == '__main__':
    # headless()
    # proxy()
    # test01()