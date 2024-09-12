from config import logging

# 设置 logging 的输出等级
# logging.basicConfig(level=logging.DEBUG)
# 设置 输出到指定的文件
# logging.basicConfig(filename='./proxy_sys/my.log',level=logging.DEBUG)

logging.debug('debug')
logging.info('info')
logging.warning('waring')
logging.error('error')
logging.critical('critical')