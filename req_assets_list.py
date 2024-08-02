# -*- coding: utf-8 -*-
# @Time     : 2024/7/29 11:52
# @Author  : Fizz
# @File     : req_assets_list.py.py
# @Description   : Hund sun


#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

# 资产列表API
url = 'https://10.163.105.97/api/v1/assets/assets/'

# HTTP头部
headers = {
    # 'Content-Type': 'application/json',  # 尽管GET请求通常不需要Content-Type，但保持与原始curl命令一致
    'Authorization': 'Token fde2a2f21a7eddd518a8e75a50eb13eb69c26dea',
    'X-JMS-ORG': '00000000-0000-0000-0000-000000000002'
}

def get_assets():
    # 发送GET请求test_api.py
    response = requests.get(url, headers=headers, verify=False)


    if response.status_code == 200:
        # 如果请求成功，打印响应内容
        my_response = response.json()
        return my_response
    else:
        # 如果请求不成功，打印错误信息和状态码
        print('status状态异常')
        print('Error:', response.status_code, response.text)

if __name__ == '__main__':
    my_assets = get_assets()
    pattern = '2.0生产'
    for i in my_assets:
        if i['type']['value'] == 'windows' and pattern.decode('utf-8') in i['nodes_display'][0]:
                print(i['address'] + '\t' + i['id'] + '\t' + i['nodes'][0]['id'])









