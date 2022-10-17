# @Project : pythonwork
# @File    : log_decorate.py
# @Author  : zhangjing
# @Time    : 2022/9/22 11:01
# @Software : Pycharm
# @Description :
import logging
import time
from functools import wraps
from logging.handlers import RotatingFileHandler


def logged(level=logging.INFO,msg=None):
    def decroate(fun):
        @wraps(fun)
        def warpper(*args,**kwargs):

            LOG_FORMAT = "%(asctime)s-%(levelname)s-%(message)s"
            DATA_FORMAT = "%m/%d/%Y %H:%M:%S %p"  # 需要定义%(asctime)s才会生效
            STR_TIME = time.strftime('%m-%d-%Y_%H-%M-%S')
            FILE_NAME = 'log/test_%s.log ' % STR_TIME  # 根据时间定义日志格式

            # 1.获取日志器
            logger = logging.getLogger('mylogger')

            # 判断当前日志器是否有文件处理器
            if not logger.handlers:
                # 日志处理器--相当与日志器的增强版本插件
                log_handler = RotatingFileHandler(FILE_NAME, encoding='utf-8',
                                                  maxBytes=1024 * 1024 * 20)  # 日志文件大于20MB自动切文件
                # 日志格式器
                log_formater = logging.Formatter(LOG_FORMAT, DATA_FORMAT)
                # 日志处理器添加格式
                log_handler.setFormatter(log_formater)  # 为日志处理器定义格式
                # 安装日志处理器
                logger.addHandler(log_handler)
                # 设置日志器输出级别
                logger.setLevel(level)

            if msg == None:
                message = '函数'+fun.__name__+'执行'
            else:
                message = msg
            try:
                print("方法执行前调用")
                res = fun(*args,**kwargs)
                logger.log(level,message)
                print("方法执行后调用")
                return res
            except Exception as e:
                logger.error(message+"异常",exc_info=True)
        return warpper
    return decroate



@logged()
def sayHello(arg):
    print(f"{arg} say hello")
    return arg

sayHello("Jane")