"""
1、日志收集器logger：
2、日志收集器级别level：
3、日志处理器准备handler： 不同记号的笔
4、日志处理器级别设置
5、logger.addHandler（handler）
6、设置日志格式format： 日期，fmt = logging.Format().
7、添加日志处理器,handler.setFormat()
"""
import logging

# 1、初始化收集器
logger = logging.getLogger('my_logger')

# 2、设置收集器级别
# 当设置为debug的时候，只有高于，等于该设置级别的才会打印
# 当设置成 warning ，只有warning， error ， critical 才会打印
logger.setLevel(logging.DEBUG)

# 3、日志处理器准备handler，
# 放到一个file文件当中
handler = logging.FileHandler('log.txt')

# 4、日志处理器级别设置
handler.setLevel(logging.DEBUG)

# 5、日志收集器和处理器关联上
logger.addHandler(handler)

# 6、设置日志格式
fmt = logging.Formatter(
    '%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s - %(process)s')

# 7、添加日志处理器
handler.setFormatter(fmt)

if __name__ == '__main__':
    logger.debug("This is a debug log.")
    logger.info("This is a info log.")
    logger.warning("This is a warning log.")
    logger.error("This is a error log.")
    logger.critical("This is a critical log.")