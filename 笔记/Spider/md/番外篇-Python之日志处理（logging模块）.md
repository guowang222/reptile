### 1. 日志相关概念
#### 1.1 日志的作用
通过log的分析，可以方便用户了解系统或软件、应用的运行情况；如果你的应用log足够丰富，也可以分析以往用户的操作行为、类型喜好、地域分布或其他更多信息；如果一个应用的log同时也分了多个级别，那么可以很轻易地分析得到该应用的健康状况，及时发现问题并快速定位、解决问题，补救损失。

简单来讲就是，我们通过记录和分析日志可以了解一个系统或软件程序运行情况是否正常，也可以在应用程序出现故障时快速定位问题。比如，做运维的同学，在接收到报警或各种问题反馈后，进行问题排查时通常都会先去看各种日志，大部分问题都可以在日志中找到答案。再比如，做开发的同学，可以通过IDE控制台上输出的各种日志进行程序调试。对于运维老司机或者有经验的开发人员，可以快速的通过日志定位到问题的根源。可见，日志的重要性不可小觑。日志的作用可以简单总结为以下3点：

- 程序调试
- 了解软件程序运行情况，是否正常
- 软件程序运行故障分析与问题定位

如果应用的日志信息足够详细和丰富，还可以用来做用户行为分析，如：分析用户的操作行为、类型洗好、地域分布以及其它更多的信息，由此可以实现改进业务、提高商业利益。

#### 1.2 日志的等级
思考下下面的两个问题：
- 作为开发人员，在开发一个应用程序时需要什么日志信息？在应用程序正式上线后需要什么日志信息？
- 作为应用运维人员，在部署开发环境时需要什么日志信息？在部署生产环境时需要什么日志信息？

在软件开发阶段或部署开发环境时，为了尽可能详细的查看应用程序的运行状态来保证上线后的稳定性，我们可能需要把该应用程序所有的运行日志全部记录下来进行分析，这是非常耗费机器性能的。当应用程序正式发布或在生产环境部署应用程序时，我们通常只需要记录应用程序的异常信息、错误信息等，这样既可以减小服务器的I/O压力，也可以避免我们在排查故障时被淹没在日志的海洋里。那么，怎样才能在不改动应用程序代码的情况下实现在不同的环境记录不同详细程度的日志呢？这就是日志等级的作用了，我们通过配置文件指定我们需要的日志等级就可以了。


#### 1.3 日志字段信息与日志格式
一条日志信息对应的是一个事件的发生，而一个事件通常需要包括以下几个内容:
- 事件发生时间
- 事件发生位置
- 事件的严重程度--日志级别
- 事件内容

### 2. logging模块简介
#### 2.1 logging模块的日志级别
logging模块默认定义了以下几个日志等级，它允许开发人员自定义其他日志级别，但是这是不被推荐的，尤其是在开发供别人使用的库时，因为这会导致日志级别的混乱。


日志等级（level）|	描述
---|---
DEBUG|	最详细的日志信息，典型应用场景是 问题诊断
INFO|	信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
WARNING|	当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
ERROR|	由于一个更严重的问题导致某些功能不能正常运行时记录的信息
CRITICAL|	当发生严重错误，导致应用程序不能继续运行时记录的信息

#### 2.2 logging模块的使用方式介绍
> logging模块定义的模块级别的常用函数


函数|	说明
---|---
logging.debug(msg, *args, **kwargs)|	创建一条严重级别为DEBUG的日志记录
logging.info(msg, *args, **kwargs)|	创建一条严重级别为INFO的日志记录
logging.warning(msg, *args, **kwargs)|	创建一条严重级别为WARNING的日志记录
logging.error(msg, *args, **kwargs)|	创建一条严重级别为ERROR的日志记录
logging.critical(msg, *args, **kwargs)|	创建一条严重级别为CRITICAL的日志记录
logging.log(level, *args, **kwargs)|	创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs)|	对root logger进行一次性配置

#### 2.3 logging.basicConfig()函数说明
> 该方法用于为logging日志系统做一些基本配置，方法定义如下：

- filename
    - 指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了
- filemode
    - 指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
- format
    - 指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。
- datefmt
    - 指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
- level
    - 指定日志器的日志级别
- stream
    - 指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
- style
    - Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
- handlers
    - Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常
#### 2.4 logging模块中定义好的可以用于format格式字符串中字段

字段/属性名称	|使用格式	|描述
---|---|---
asctime|	%(asctime)s|	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
created|	%(created)f|	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
relativeCreated|	%(relativeCreated)d|	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
msecs|	%(msecs)d|	日志事件发生事件的毫秒部分
levelname|	%(levelname)s|	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
levelno|	%(levelno)s|	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
name|	%(name)s|	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
message|	%(message)s|	日志记录的文本内容，通过 msg % args计算得到的
pathname|	%(pathname)s|	调用日志记录函数的源码文件的全路径
filename|	%(filename)s|	pathname的文件名部分，包含文件后缀
module|	%(module)s|	filename的名称部分，不包含后缀
lineno|	%(lineno)d|	调用日志记录函数的源代码所在的行号
funcName|	%(funcName)s|	调用日志记录函数的函数名
process|	%(process)d|	进程ID
processName|	%(processName)s|	进程名称，Python 3.1新增
thread|	%(thread)d|	线程ID
threadName|	%(thread)s|	线程名称

#### 2.5 举例
```
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

DATE_FORMAT = "[%Y/%m/%d] %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT,datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
```