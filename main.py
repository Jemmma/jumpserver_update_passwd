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

# 密码模块初始化
new_passwd = set_random_passwd.generate_passwd()
# 资产列表获取
all_assets = req_assets_list.get_assets()
print(all_assets)
# CMD命令设置


error_list = []

def set_passwd(old_passwd, group, code_func='ipconfig |findstr "10."'):
    print('session 1')
    print('复杂度密码已创建：' + new_passwd)
    print('session 2')
    print('开始远程登录机器执行function')
    if code_func == '1':
        code_func = 'net user administrator "{}"'.format(new_passwd)
    for i in all_assets:
        if i['type']['value'] == 'windows' and group in i['nodes_display'][0]:
            print(i['address'] + '\t' + i['id'])
            try:
                remote_cmd.winCMD(hostip=i['address'], username='administrator', password=old_passwd, code_func=code_func)
            except Exception as InvalidCredentialsError:
                try:
                    code_func_new = 'net user hundsun "{}"'.format(new_passwd)
                    remote_cmd.winCMD(hostip=i['address'], username='hundsun', password=old_passwd, code_func=code_func_new)
                except Exception as InvalidCredentialsError:
                    error_list.append(i['address'])
                continue

    print('捕获到异常的列表为：')
    print(error_list)


if __name__ == '__main__':
    #old_passwd = 'Qq5#6qOLozBE'
    #group = '3.0UAT'
    #code_func = 'ipconfig |findstr "10."'
    old_passwd = sys.argv[1]
    group = sys.argv[2]
    code_func = sys.argv[3]
    set_passwd(old_passwd=old_passwd, group=group, code_func=code_func)
