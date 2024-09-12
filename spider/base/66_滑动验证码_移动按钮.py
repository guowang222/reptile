from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from hua_dong import distance,track
from time import sleep
def save_img():

    url = 'https://www.sf-express.com/cn/sc/dynamic_function/waybill/#search/bill-number/SF1406050054883'
    chrome = webdriver.Chrome(executable_path='../tools/chromedriver.exe')
    chrome.get(url)
    wait = WebDriverWait(chrome,5)
    try:
        wait.until(EC.presence_of_element_located((By.ID,'tcaptcha_popup')))
        # 切换frame
        chrome.switch_to.frame('tcaptcha_popup')
        # 获取图片src
        img = chrome.find_element_by_id('slideBkg')
        # img.screenshot('temp.png')
        img_src = img.get_attribute('src')[:-1]
        # 下载图片
        down_img(img_src+'1','cpt1.png')
        down_img(img_src+'2','cpt2.png')
        
        # 获取移动的距离
        tmp_d = distance.get_long()
        # 获取移动轨迹
        tmp_track = track.get_track(tmp_d-12)
        # 滑动按钮
            # 选中按钮
        button = chrome.find_element_by_id('tcaptcha_drag_button')
        webdriver.ActionChains(chrome).click_and_hold(button).perform()
            # 拖动按钮-按照轨迹拖动
        for t in tmp_track:
            webdriver.ActionChains(chrome).move_by_offset(xoffset=t, yoffset=0).perform()
        # 释放按钮
        webdriver.ActionChains(chrome).release().perform()
        # 休眠2秒
        sleep(2)
        # 关闭浏览器
        chrome.quit()
    except Exception as e:
        chrome.quit()

def down_img(url,filename):
    print(url)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
    resp = requests.get(url,headers=headers)
    with open(f'./imgs/{filename}','wb') as f:
        f.write(resp.content)
if __name__ == '__main__':
    save_img()
    # selenium\webdriver\common\actions\pointer_input.py