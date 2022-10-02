import logging
import sys
from logging.handlers import HTTPHandler

# 创建日志对象
logger = logging.getLogger('logger')

# 将日志输出到文件 FileHandler
# file_handler = logging.FileHandler(filename='test.log', mode='w', encoding='utf-8')
# file_fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
# file_handler.setFormatter(file_fmt)
# file_handler.setLevel(level=logging.INFO)
# logger.addHandler(file_handler)

# 将日志输出到控制台 StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
# stream_fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
stream_fmt = logging.Formatter(fmt='%(asctime)s %(levelname)s %(thread)d  %(threadName)s %(funcName)s %(message)s')
stream_handler.setFormatter(stream_fmt)
stream_handler.setLevel(level=logging.INFO)
logger.addHandler(stream_handler)


a = {'a': '1', 'b': '2', 'c': '3'}
logging.error("循环map key")
for key in a:
    print(key + ':' + a[key])

logging.error("循环map keys")

for key in a.keys():
    print(key + ':' + a[key])

logging.error("循环map values")

for value in a.values():
    print(value)

logging.error("循环map items")

for kv in a.items():
    print(kv)

logging.error("循环map key value items")

for key, value in a.items():
    print(key + ':' + value)

for (key, value) in a.items():
    print(key + ':' + value)
