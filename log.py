# -*- coding: utf-8 -*-
# @Time     : 2024/8/1 13:37
# @Author  : Fizz
# @File     : log.py.py
# @Description   : Hund sun

import os
import logging
from logging.handlers import TimedRotatingFileHandler
import datetime

# 定义日志文件的路径和名称
log_dir = 'logs'

# 检查并创建日志文件目录
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 定义日期格式
Today = datetime.date.today()

class TimedRotatingLogger:
    def __init__(self, name, log_dir, level=logging.INFO):
        # 创建一个logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # 创建一个handler，用于写入日志文件
        file_handler = TimedRotatingFileHandler(
            "%s/%s_%s.log" % (log_dir, name, Today), when='D', interval=1, backupCount=20)
        # 当执行多天需要自动切割时
        # file_handler.suffix = "%Y-%m-%d %H%M%S.log"
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        # 创建一个handler，用于将日志输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        # 添加handler到logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger




if __name__ == '__main__':
    logger_wrapper = TimedRotatingLogger('jumpserver_update_passwd', log_dir)
    logger = logger_wrapper.get_logger()

