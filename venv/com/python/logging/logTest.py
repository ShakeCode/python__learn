import logging

'''
%c，格式化字符及其ASCII码
%s，格式化字符串
%d，格式化整数
%u，格式化无符号整数
%o，格式化无符号八进制数6、%f,浮点数（float）占位符，也可以表示整数（int），默认保留小数点后6位
'''

logFile = 'mylog.log'
formatStr11 = '%(asctime)s - %(name)s - process_id: %(process)s - thread_id: %(thread)d - %(filename)s - %(levelname)s - %(lineno)d: %(message)s'
formatStr22 = '%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s'
logging.basicConfig(filename=logFile, format=formatStr11,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger()
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter(formatStr11))
logger.addHandler(streamHandler)
# fileHandler = logging.FileHandler(logFile, mode='a')
# 获取当前路径，绝对路径
# path = os.path.abspath('.')
# fileHandler = handlers.TimedRotatingFileHandler(filename=path+'\\send.log', when='D')
# logger.addHandler(fileHandler)

logger.error('param url:{0}'.format('baidu.com'))
logger.info("设备ID=%s ,  计划时间=%s分钟", 11, 5)
logger.info("这是数字%d", 800)
logger.info("这是小数%f", 800)
logger.info("这是无符号整数%u", 800)
logger.info("这是无符号八进制%o", 21321)

# 另外用%s,也可输出其他非字符串的数据：

logger.info("这是time 模块 %s", 111)
logger.info("这是threading 模块 %s", 2222)
