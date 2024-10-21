#!/usr/bin/env python
# encoding: utf-8

import requests
import base64
import json
from auth_util import gen_sign_headers

# 请注意替换APP_ID、APP_KEY
APP_ID = '3032265746'
APP_KEY = 'iULreUHzWwPqMZph'
URI = '/api/v1/task_submit'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'

def submit(content):
   params = {} #空字典
   data = { #初始化字典，包含四个键值对
    'height': 768,
    'width': 576,
    'prompt': content,
    'styleConfig': '8fe3d641be3e589dad231dc6c3b1429a'
   }
   #请求头
   headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
   headers['Content-Type'] = 'application/json'#添加一个键值对，然后值得内容为json
   #完整得URL
   url = 'http://{}{}'.format(DOMAIN, URI)
   #使用 requests 库发送一个 POST 请求到 url，请求的数据是 data 字典的 JSON 格式
   #表示，请求头是 headers。响应被存储在 response 变量中
   response = requests.post(url, data=json.dumps(data), headers=headers)
   if response.status_code == 200:  #检查响应状态是否为 200，即请求成功
       print(response.json())
       print(response.json()['result']['task_id'])
       return response.json()['result']['task_id']  # 确保这里返回的是字符串
   else:  #如果请求失败，打印出响应状态码和响应内容
       print(response.status_code, response.text)
       return None
