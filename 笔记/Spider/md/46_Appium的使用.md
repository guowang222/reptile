## 利用appium提取数据



### 1 appium-python-client使用

 #### 1.1 安装appium-python-client模块

```shell
pip install appium-python-client
```

#### 1.2 初始化以及获取移动设备分辨率

> 完成代码如下，并运行代码查看效果：如果模拟器中抖音app被启动，并打印出模拟设备的分辨率则成功

```
from appium import webdriver

# 初始化配置，设置Desired Capabilities参数
desired = {
  "platformName": "Android",
  "appPackage": "com.jingdong.app.mall",
  "appActivity": "com.jingdong.app.mall.MainFrameActivity",
  "platformVersion": "5.1.1",
  "deviceName": "OPPO R11 Plus"
}
# 指定Appium Server
server = 'http://localhost:4723/wd/hub'
# 新建一个driver
driver = webdriver.Remote(server, desired)
# 获取模拟器/手机的分辨率(px)
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print(width, height)
```

- 移动设备分辨率

  - driver.get_window_size()['width']

  - driver.get_window_size()['height']

#### 1.3 获取标签

通过APPium获取xpath, 根据selenium用法开发即可

```python
find_element_by_id
find_elements_by_id
find_element_by_xpath
find_elements_by_xpath
```

#### 1.4 获取内容

```python
element.text
```

### 2 案例实战

#### 2.1起动软件

```python
desired = {
  "platformName": "Android",
  "appPackage": "cn.kuwo.player",
  "appActivity": "cn.kuwo.player.activities.EntryActivity",
  "platformVersion": "5.1.1",
  "deviceName": "OPPO R11 Plus"
}

server = 'http://localhost:4723/wd/hub'

# 新建一个driver
driver = webdriver.Remote(server, desired)
```

#### 2.2 设置等待

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 15)
```



#### 2.3 操控元素

```python

ty_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]'
wait.until(EC.presence_of_element_located((By.XPATH,ty_xpath)))
driver.find_element_by_id(ty_id).click()

close_id ='cn.kuwo.player:id/iv_close'
wait.until(EC.presence_of_element_located((By.ID,close_id)))
driver.find_element_by_id(close_id).click()

pai_hang_xpath ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.ImageView'
wait.until(EC.presence_of_element_located((By.XPATH,pai_hang_xpath)))
pai_hang = driver.find_element_by_xpath(pai_hang_xpath)
pai_hang.click()

dou_yin_xpath ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
wait.until(EC.presence_of_element_located((By.XPATH,dou_yin_xpath)))
dou_yin = driver.find_element_by_xpath(dou_yin_xpath)
dou_yin.click()

```



#### 2.4 滑动屏幕获取数据

```python
flag  = False

width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
start_x = end_x = int(width*0.5)
start_y = int(height*0.75)
end_y  = int(height*0.25)

music = []

while not flag:
    m_name_xpath3 ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView'
    m_name3 = driver.find_elements_by_xpath(m_name_xpath3)
    info = [i.text for i in m_name3]

    for c in info:
        if c not in music:
            music.append(c)
            print(c)

    driver.swipe(start_x, start_y, end_x, end_y)
    sleep(1)
    try:
        end_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView'
        flag = driver.find_element_by_xpath(end_xpath)
    except Exception  as e:
        flag = False

m_name_xpath3 ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView'
m_name3 = driver.find_elements_by_xpath(m_name_xpath3)
info = [i.text for i in m_name3]

for c in info:
    if c not in music:
        music.append(c)
        print(c)
```

