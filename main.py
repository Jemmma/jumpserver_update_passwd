# -*- coding: utf-8 -*-
# @Time     : 2024/7/29 11:53
# @Author  : Fizz
# @File     : main.py
# @Description   : Hund sun

# coding=utf-8

import set_random_passwd
import remote_cmd
import req_assets_list
import sys
from log import *

# 引用日志模块
logger_wrapper = TimedRotatingLogger('jumpserver_update_passwd', log_dir)
logger = logger_wrapper.get_logger()

# 密码模块初始化
new_passwd = set_random_passwd.generate_passwd()
# 资产列表获取
all_assets = req_assets_list.get_assets()

# 未执行成功的列表
update_error_list = []
remote_error_list = []

def set_passwd(old_passwd, group, code_func='ipconfig |findstr "10."'):
    logger.info('------Parse 1------')
    logger.info('加载初始变量[旧密码]: %s' % old_passwd)
    logger.info('加载初始变量[主机组]: %s' % group)
    logger.info('加载初始变量[远程指令]: %s' % code_func)
    logger.info('创建具有复杂度的[密码]: %s' % new_passwd)

    logger.info('------Parse 2------')
    logger.info('开始处理远程命令模块')

    if code_func == '1':
        update_code = 'net user administrator "{}"'.format(new_passwd)
        logger.info('改密模式[administrator]: %s' % update_code)
        for i in all_assets:
            if i['type']['value'] == 'windows' and group in i['nodes_display'][0]:
                print('------------------------------')
                try:
                    update_result = remote_cmd.winCMD(hostip=i['address'], username='administrator', password=old_passwd,
                                                code_func=update_code)
                    logger.info('update_result: \n %s' % update_result.std_out)
                except Exception, InvalidCredentialsError:
                    logger.info('更改[主机 %s]的administrator密码错误' % (i['address']))
                    update_code_new = 'net user hundsun "{}"'.format(new_passwd)
                    logger.info('更改改密模式为[hundsun]: %s' % update_code_new)
                    try:
                        update_result2 = remote_cmd.winCMD(hostip=i['address'], username='hundsun', password=old_passwd,
                                                    code_func=update_code_new)
                        logger.info('update_result: \n %s' % update_result2.std_out)
                    except Exception, InvalidCredentialsError:
                        update_error_list.append(i['address'])
    else:
        logger.info('执行远程命令模式[administrator]: %s' % code_func)
        for i in all_assets:
            if i['type']['value'] == 'windows' and group in i['nodes_display'][0]:
                print('------------------------------')
                try:
                    remote_result = remote_cmd.winCMD(hostip=i['address'], username='administrator', password=old_passwd,
                                                code_func=code_func)
                    logger.info('remote_result: \n %s' % remote_result.std_out)
                except Exception, InvalidCredentialsError:
                    logger.info('使用administrator用户对[主机 %s]执行远程命令操作失败' % (i['address']))
                    logger.info('更改远程命令模式[hundsun]: %s' % code_func)
                    try:
                        remote_result2 = remote_cmd.winCMD(hostip=i['address'], username='hundsun', password=old_passwd,
                                                    code_func=code_func)
                        logger.info('remote_result: \n %s' % remote_result2.std_out)
                    except Exception, InvalidCredentialsError:
                        remote_error_list.append(i['address'])

    logger.info('------Parse 3------')
    if len(update_error_list) > 0:
        logger.info('改密模式中异常的主机列表有：' + "".join(str(update_error_list)))
    elif len(remote_error_list) > 0:
        logger.info('远程命令模式中异常的主机列表有：' + "".join(str(remote_error_list)))
    else:
        logger.info('success，无未正常执行远程命令的主机：')


if __name__ == '__main__':
    # old_passwd = 'Qq5#6qOLozBE'
    # group = '3.0UAT'
    # code_func = 'ipconfig |findstr "10."'
    old_passwd = sys.argv[1]
    group = sys.argv[2]
    code_func = sys.argv[3]
    set_passwd(old_passwd=old_passwd, group=group, code_func=code_func)
