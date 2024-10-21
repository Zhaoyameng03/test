#!/usr/bin/env python
# encoding: utf-8
#����ͼƬ��url������ͼƬ��base64���봮
'''
url��ͬ�����������URL
requests����������� data �ֵ�� JSON ��ʽ��prompt)

���ظ�ʽ��
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

# ��ע���滻APP_ID��APP_KEY
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
    'prompt': 'һֻ��߻���è',
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