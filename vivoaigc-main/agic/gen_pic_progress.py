#!/usr/bin/env python
# encoding: utf-8
'''
请求参数url以及task_id
返回：
{
  'code': 200,
  'msg': 'successful',
  'result': {
    'finished': True,
    'images_gaia_key': [
      'prd-074f65f8845e5967a4e05871f9884934-0.jpg'
    ],
    'images_info': {
      'prompt': '一只梵高画的猫'
    },
    'images_url': [
      'https://ai-painting-image.vivo.com.cn/ai-painting/prd-074f65f8845e5967a4e05871f9884934-0.jpg'
    ],
    'queue_ahead': 0,
    'status': 2,
    'task_eta': 0
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
URI = '/api/v1/task_progress'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'GET'
	
def progress():
   params = {
       'task_id': 'd98dea86bf3258799fd33f0e776e9868'
   }
   headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

   uri_params = ''
   for key, value in params.items():
       uri_params = uri_params + key + '=' + value + '&'
   uri_params = uri_params[:-1]

   url = 'http://{}{}?{}'.format(DOMAIN, URI, uri_params)
   print('url:', url)
   response = requests.get(url, headers=headers)
   if response.status_code == 200:
       print(response.json())
   else:
       print(response.status_code, response.text)

if __name__ == '__main__':
   progress()