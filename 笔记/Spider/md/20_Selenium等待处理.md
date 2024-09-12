### 1 等待
#### 1.1 强制等待
> 使用 time.sleep

作用：

当代码运行到强制等待这一行的时候，无论出于什么原因，都强制等待指定的时间，需要通过time模块实现

优点：简单

缺点：无法做有效的判断，会浪费时间

#### 1.2 隐式等待
> 到了一定的时间发现元素还没有加载，则继续等待我们指定的时间，如果超过了我们指定的时间还没有加载就会抛出异常，如果没有需要等待的时候就已经加载完毕就会立即执行

优点： 设置一次即可

缺点：必须等待加载完成才能到后续的操作，或者等待超时才能进入后续的操作

```python
from selenium import webdriver
url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
print(driver.find_element_by_class_name('next'))
print(driver.page_source)
```

#### 1.3 显示等待
> 指定一个等待条件，并且指定一个最长等待时间，会在这个时间内进行判断是否满足等待条件，如果成立就会立即返回，如果不成立，就会一直等待，直到等待你指定的最长等待时间，如果还是不满足，就会抛出异常，如果满足了就会正常返回

优点：专门用于对指定一个元素等待，加载完即可运行后续代码

缺点：多个元素都需要要单独设置等待


```python
    url = 'https://www.guazi.com/nj/buy/'
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver,10,0.5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'next')))
    print(driver.page_source)
``` 