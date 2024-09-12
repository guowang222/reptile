### selenium 处理下拉框

下拉框是我们最常见的一种页面元素，对于一般的元素，我们只需要一次就定位，但下拉框里的内容需要进行两次定位，先定位到下拉框，再定位到下拉框内里的选项。


**drop_down.html**

```html
<html>
    <body>
        <select id="ShippingMethod" onchange="updateShipping(options[selectedIndex]);" name="ShippingMethod">
            <option value="12.51">UPS Next Day Air ==> $12.51</option>
            <option value="11.61">UPS Next Day Air Saver ==> $11.61</option>
            <option value="10.69">UPS 3 Day Select ==> $10.69</option>
            <option value="9.03">UPS 2nd Day Air ==> $9.03</option>
            <option value="8.34">UPS Ground ==> $8.34</option>
            <option value="9.25">USPS Priority Mail Insured ==> $9.25</option>
            <option value="7.45">USPS Priority Mail ==> $7.45</option>
            <option value="3.20" selected="">USPS First Class ==> $3.20</option>
        </select>
    </body>
</html>
```

将上面的代码保存成html通过浏览器打开会看到一个最简单常见的下拉框，下拉列表有几个选项。

现在我们来选择下拉列表里的$10.69

```python
driver= webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('drop_down.html')
driver.get(file_path)
time.sleep(2)
m=driver.find_element_by_id("ShippingMethod")
m.find_element_by_xpath("//option[@value='10.69']").click()
time.sleep(3)
driver.quit()
```

有时，页面可能要弹窗口。只需要去定位弹窗上的“确定”按钮即可：

- 切换至弹窗

```python
driver.switch_to_alert().accept()

# switch_to_alert()  
# 焦点集中到页面上的一个警告（提示）
# accept()
# 接受警告提示
```