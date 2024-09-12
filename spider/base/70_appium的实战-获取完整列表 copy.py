from appium import webdriver
from time import sleep

server = 'http://localhost:4723/wd/hub'
desired = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "SM-N976N",
  "appPackage": "cn.kuwo.player",
  "appActivity": "cn.kuwo.player.activities.EntryActivity"
}
# 创建模拟器
# 协议按钮
driver = webdriver.Remote(server,desired)
# 获取模拟器的分辨率
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']

start_x = end_x = int(width*0.5)
start_y = int(height*0.75)
end_y = int(height*0.25)

a_button_id = 'cn.kuwo.player:id/tv_ok'
a_button = driver.find_element_by_id(a_button_id)
a_button.click()
# 权限按钮
r_btton_id = 'cn.kuwo.player:id/tv_ok'
r_btton = driver.find_element_by_id(r_btton_id)
r_btton.click()

r_btton_id2 = 'com.android.packageinstaller:id/permission_allow_button'
r_btton2 = driver.find_element_by_id(r_btton_id2)
r_btton2.click()


# 关闭登录按钮
close_btton_id = 'cn.kuwo.player:id/iv_close'
close_btton = driver.find_element_by_id(close_btton_id)
close_btton.click()

pai_hang_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.ImageView'
pai_hang = driver.find_element_by_xpath(pai_hang_xpath)
pai_hang.click()

music_list_xpath ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[4]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout'
music_list = driver.find_element_by_xpath(music_list_xpath)
music_list.click()

# tmp1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView'
name_list_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView'

# m1 = driver.find_element_by_xpath(tmp1).text
# print(m1)
music_name_list = []
flag = False
while not flag:
# 滑动屏幕
  
  name_list = [ele.text for ele in driver.find_elements_by_xpath(name_list_xpath)]
  for m in name_list:
    if m not in music_name_list:
      music_name_list.append(m)
      print(m)
  sleep(0.5)
  driver.swipe(start_x, start_y, end_x, end_y)
  end_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView'
  try:
    flag = driver.find_element_by_xpath(end_xpath)
  except Exception as e:
    flag = False
name_list = [ele.text for ele in driver.find_elements_by_xpath(name_list_xpath)]
for m in name_list:
  if m not in music_name_list:
    music_name_list.append(m)
    print(m)