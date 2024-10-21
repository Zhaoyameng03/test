#!/usr/bin/env python
# encoding: utf-8
#输入图片的url，返回图片的base64编码串
'''
url不同是任务里面的URL
requests请求的数据是 data 字典的 JSON 格式（prompt)

返回格式：
{
  'code': 200,
  'msg': 'successful',
  'result': {
    'task_id': '074f65f8845e5967a4e05871f9884934'
  }
}
'''
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

def submit():
   params = {}
   data = {
    'height': 768,
    'width': 576,
    'prompt': '一只梵高画的猫',
    'styleConfig': '55c682d5eeca50d4806fd1cba3628781'
   }

   headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
   headers['Content-Type'] = 'application/json'

   url = 'http://{}{}'.format(DOMAIN, URI)
   response = requests.post(url, data=json.dumps(data), headers=headers)
   if response.status_code == 200:
       print(response.json())
   else:
       print(response.status_code, response.text)

if __name__ == '__main__':
   submit()