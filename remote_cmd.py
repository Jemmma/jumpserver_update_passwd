# -*- coding: utf-8 -*-
# @Time     : 2024/7/29 11:50
# @Author  : Fizz
# @File     : remote_cmd.py
# @Description   : Hund sun


# !/usr/bin/python
# -*- coding: utf-8 -*-

import winrm
import sys
from log import *

reload(sys)
sys.setdefaultencoding('utf-8')
# set default encoding to utf-8


# # 引用日志模块
# logger_wrapper = TimedRotatingLogger('jumpserver_update_passwd', log_dir)
# logger = logger_wrapper.get_logger()

def winCMD(hostip='hostip', username='username', password='password', code_func='code_func' ):
    '''
    :param hostip:
    :param username:
    :param password:
    :return:
    '''

    winconn = winrm.Session('http://' + hostip + ':5985/wsman', auth=(username, password), transport='ntlm')
    # logger.info('processing: %s' % (code_func))
    ret = winconn.run_cmd(code_func)
    # print("result:" + ret.std_out.decode())

    # logger.info('result: \n %s' % (ret.std_out))
    return(ret)
    # return(ret)

if __name__ == '__main__':
    a = winCMD('10.25.7.45', 'administrator', 'hundsun@2022', code_func='ipconfig')
    print(a.std_out)



