# -*- coding: utf-8 -*-
# @Time     : 2024/7/29 11:53
# @Author  : Fizz
# @File     : set_random_passwd.py.py
# @Description   : Hund sun


# !/usr/bin/python
# -*- coding: utf-8 -*-

import random
import string


def generate_passwd():
    # 设定密码长度
    length = 12

    # 设定字符类型
    uppercase = string.ascii_uppercase  # 大写字母
    lowercase = string.ascii_lowercase  # 小写字母
    digits = string.digits  # 数字
    special_chars = '!$#@_'  # 特殊字符

    # 设定每种字符类型在密码中至少存在一个
    password = (random.choice(uppercase) +
                random.choice(lowercase) +
                random.choice(digits) +
                random.choice(special_chars))

    # 计算剩余字符总数
    len_passwd = length - len(password)

    # 随机获取剩余字符
    all_str = uppercase + lowercase + digits + special_chars

    # 随机剩余字符
    for i in range(len_passwd):
        password = password + ''.join(random.choice(all_str))

    # 返回符合密码复杂度的密码
    return(password)


if __name__ == '__main__':
    my_passwd = generate_passwd()
    print('现随机生成复杂度密码:' + my_passwd)