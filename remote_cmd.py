# -*- coding: utf-8 -*-
# @Time     : 2024/7/29 11:50
# @Author  : Fizz
# @File     : remote_cmd.py
# @Description   : Hund sun


# !/usr/bin/python
# -*- coding: utf-8 -*-

import winrm
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# set default encoding to utf-8

def winCMD(hostip='hostip', username='username', password='password', code_func='code_func' ):
    '''
    :param hostip:
    :param username:
    :param password:
    :return:
    '''

    winconn = winrm.Session('http://' + hostip + ':5985/wsman', auth=(username, password), transport='ntlm')
    print("processing:" + code_func)
    ret = winconn.run_cmd(code_func)
    # print("result:" + ret.std_out.decode())
    print("result:" + ret.std_out)


if __name__ == '__main__':
    winCMD('128.0.0.130', 'administrator', 'DKd@fi7Iw6Ju', code_func='ipconfig')



