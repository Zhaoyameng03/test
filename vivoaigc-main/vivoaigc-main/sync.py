# encoding: utf-8
import uuid
import time
import requests
from auth_util import gen_sign_headers

# 请替换APP_ID、APP_KEY
APP_ID = '3032265746'
APP_KEY = 'iULreUHzWwPqMZph'
URI = '/vivogpt/completions'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'


def sync_vivogpt():
    params = {
        #随机生成的 UUID 作为 requestId。这个 UUID 通常用于标识和跟踪请求。
        'requestId': str(uuid.uuid4())
    }
    print('requestId:', params['requestId'])

    data = {
        'prompt': '望庐山瀑布',
        'model': 'vivo-BlueLM-TB',
        'sessionId': str(uuid.uuid4()),
        'systemPrompt':'你精通所有古诗词，当输入诗句或者题目时你用白话文直接回复其所描绘出的场景',
        'extra': {
            'temperature': 0.9
        }
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'
    #记录开始时间
    start_time = time.time()
    url = 'https://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, json=data, headers=headers, params=params)

    if response.status_code == 200:
        #如果状态码为 200，代码会尝试将响应内容解析为 JSON 对象。
        #这假设服务器返回的是一个 JSON 格式的响应体。
        res_obj = response.json()
        print(f'response:{res_obj}')
        #JSON 对象中的 'code' 字段的值为 0，通常表示操作或请求成功。
        #如果 'data' 字段存在并且其值为真（例如，不是 None、空字符串等），则条件为真
        if res_obj['code'] == 0 and res_obj.get('data'):
            #从 JSON 对象的 'data' 字段提取 'content' 字段的值，并存储在变量 content 中
            content = res_obj['data']['content']
            print(f'final content:\n{content}')

            
            return content
    #这段代码的主要目的是检查 HTTP 响应的状态码，然后解析响应内容为 JSON 对象。
    #它检查 JSON 对象中的特定字段以确定是否成功提取了所需的数据（'content' 字段）。
    #如果成功，它返回该数据。如果失败，它打印出响应的状态码和内容。   
    else:
        print(response.status_code, response.text)
    end_time = time.time()
    timecost = end_time - start_time
    print('请求耗时: %.2f秒' % timecost)

if __name__ == '__main__':
    sync_vivogpt()