## Appium环境搭建

有的APP需要反编译，分析加密算法后，再获取信息。有的APP还需要脱壳，再需要反编译，分析加密算法。但要再了解这些问题，还是需要花些时间的，所以在些，我们可以通过移动端对APP的控制，来解析数据获取数据。



### 1. Android SDK安装

SDK:(software development kit) 软件开发工具包。是软件开发工程师用于为特定的软件包、软件框架、硬件平台、操作系统等建立应用软件的开发工具集合。

Android SDK 指的是Androdid专属的软件开发工具包



#### 1.1  安装java JDK

##### 1.1.1 下载

点击进入官网下载页面[Java SE Development Kit 8 - Downloads (oracle.com)](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)

![image-20210807153712270](..\img\image-20210807153712270.png)



![image-20210807153757498](..\img\image-20210807153757498.png)

![image-20210807153955658](..\img\image-20210807153955658.png)

```python
账号 1 :amador.sun@foxmail.com
密码:1211WaN!

账号 2 :amador.sun@qq.com
密码:1211WaN!

账号 3 :hellooracle123@qq.com
密码:1211WaN!

账号 4 :javacno.1@qq.com
密码:1211WaN!

账号 5 :oracle-01@qq.com
密码:1211WaN!

账号 6 :oracle-02@qq.com
密码:1211WaN!
```

##### 1.1.2 安装

![image-20210807154316787](..\img\image-20210807154316787.png)

![image-20210807154422209](..\img\image-20210807154422209.png)

##### 1.1.3 配置环境变量

JAVA_HOME

PATH

![image-20210807155009009](..\img\image-20210807155009009.png)



![image-20210807155150138](..\img\image-20210807155150138.png)

#### 1.2 安装android SDK

1. 进入网站 https://www.androiddevtools.cn/

2. 依次点击 AndroidSDK 工具>> SDK Tools>>会跳转到以下界面，Windows建议选择.exe后缀

   ![image-20210807160326592](..\img\image-20210807160326592.png)



3. 安装环境变量

   ANDROID_HOME

   PATH

![image-20210807162408002](..\img\image-20210807162408002.png)

![image-20210807162731621](..\img\image-20210807162731621.png)

#### 1.3 adb

 adb (Android Debug Bridge) 是一个通用命令行工具，其允许您与模拟器实例或连接的Android设备进行通信。它可为各种设备操作提供便利，如果安装和调试应用

![image-20210807191038780](..\img\image-20210807191038780.png)

在 sdk中安装好后，会在生成到platforms-tools中



**注意：adb 链接手机 要开起开发模式**



**同步 安装adb 与 模拟器 等级**

> 将 sdk manager 中安装的 `adb.exe`, `AdbWinApi.dll`,`AdbWinUsbApi.dll` copy 到根目录中。 adb.exe 多拷贝一份 替换 nox_adb.exe 文件即可

![image-20210807191136345](..\img\image-20210807191136345.png)



> 若是不 adb devices中没有显示设备，就可以通过 adb connect 127.0.0.1:[62001/62025]
>
> 





### 2. Appium 介绍

![img](..\img\09.png)

Appium 是一个开源工具，用于自动化 iOS 手机、 Android 手机和 Windows 桌面平台上的原生、移动 Web 和混合应用。**原生应用**指那些用 iOS、 Android 或者 Windows SDKs 编写的应用

重要的是，Appium 是跨平台的：它允许你用同样的 API 对多平台（iOS、Android、Windows）写测试。做到在 iOS、Android 和 Windows 测试套件之间复用代码

GitHub：https://github.com/appium/appium

官方网站：[http://appium.io](http://appium.io/)

appium 类库封装了标准的Selenium客户端库。

Appium服务端定义了官方协议的扩展，为appium用户提供了方便的接口来执行各种设备动作



#### 2.1 Appium 原理

![image-20210803200026118](..\img\image-20210803200026118.png)





#### 2.2 开启Appium并配置运行

1. 获取app包名和进程名

   - 打开夜神模拟器中的浏览器
   - 在adb连接正确的情况下，在夜神模拟器安装目录的bin目录下的cmd中输入`adb shell`
   - 进入adb shell后输入 `logcat | grep cmp=`
   - `com.jingdong.app.mall`要运行的app包名
   - `com.jingdong.app.mall.MainFrameActivity`要运行的APP名

**参数配置**

- platformName 系统名 `Android`
- platformVersion 系统版本 `5.1.1`
- deviceName 手机型号 `SM-G955F` 或者 `192.168.30.192:62001`
- appPackage app的包名 `com.android.browser`
- appActivity app的进程名 `.BrowserActivity`
  - 可以通过 adb shell 获取值
    - `logcat | grep cmp=`
    - 打开程序

![image-20210807234810354](..\img\image-20210807234810354.png)

[所需的功能 - 应用 (appium.io)](http://appium.io/docs/en/writing-running-appium/caps/#appium-desired-capabilities)

