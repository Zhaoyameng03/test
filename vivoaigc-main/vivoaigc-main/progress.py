#!/usr/bin/env python
# encoding: utf-8

import requests
import base64
import json
from auth_util import gen_sign_headers

# 请注意替换APP_ID、APP_KEY
APP_ID = '3032265746'
APP_KEY = 'iULreUHzWwPqMZph'
URI = '/api/v1/task_progress'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'GET'

def progress(task_id): #函数参数
    params = {
        'task_id': task_id  #键值对
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

    uri_params = ''#初始化
    for key, value in params.items():
        uri_params = uri_params + key + '=' + value + '&'
    uri_params = uri_params[:-1]#使用切片操作来移除最后一个多余的&字符。

    url = 'http://{}{}?{}'.format(DOMAIN, URI, uri_params)
    print('url:', url)
    #使用requests库（常用的Python HTTP库）发送一个GET请求到构建的URL，
    #并使用之前生成的headers作为请求头
    response = requests.get(url, headers=headers)
    if response.status_code == 200:#HTTP响应的状态码是200（表示请求成功）
        print(response.json())#打印响应的JSON内容，
        #并尝试打印JSON中result键下的images_url值
        print(response.json()['result']['images_url'])
    else:
        #响应的状态码不是200，则打印状态码和响应的文本内容。
        print(response.status_code, response.text)


if __name__ == '__main__':
    progress()