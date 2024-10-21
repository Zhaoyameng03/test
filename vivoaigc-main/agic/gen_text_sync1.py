# encoding: utf-8
# @Time    : 2021/8/31 16:57
'''
请求参数url和请求参数body prompt
返回：
{
  "code": 0,
  "data": {
    "sessionId": "7b666a7aa0a811eeb5aad8bbc1c0d6bd",
    "requestId": "891483e6-3503-45db-808a-ab28672cc175",
    "content": "周海媚并没有去世，她依然活跃在演艺圈中。周海媚是中国香港影视女演员，出生于1966年，曾经在多部电视剧和电影中担任主演，如《倚天屠龙记》、《杨门女将之军令如山》等。",
    "provider": "vivo",
    "model": "vivo-BlueLM-TB"
  },
  "msg": "done."
}
'''
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
        'requestId': str(uuid.uuid4())
    }
    print('requestId:', params['requestId'])
    messages = [
        {
            "role": "user",
            "content": "望庐山瀑布"
        },
        {
            "role": "assistant",
            "content": "中国四大名著是指《红楼梦》、《西游记》、《水浒传》和《三国演义》。这四部小说在中国文学史上具有极高的地位，被广泛传阅和研究。"
        },
        {
            "role": "user",
            "content": "这四部小说的作者分别是谁？"
        }
    ]

    data = {
        'messages': messages,
        #'messages': ["望庐山瀑布", "这句古诗来着哪里", "全文是什么", "古诗的全文意思是什么", "如果你是诗人，描述一下你所处的场景"],
        'model': 'vivo-BlueLM-TB',
       # 'systemPrompt':'你精通所有古诗词，当输入诗句或者题目时你用白话文直接回复其所描绘出的场景',
        'sessionId': str(uuid.uuid4()),
        'extra': {
            'temperature': 0.9
        }
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    start_time = time.time()
    url = 'https://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, json=data, headers=headers, params=params)

    if response.status_code == 200:
        res_obj = response.json()
        print(f'response:{res_obj}')
        if res_obj['code'] == 0 and res_obj.get('data'):
            content = res_obj['data']['content']
            print(f'final content:\n{content}')
    else:
        print(response.status_code, response.text)
    end_time = time.time()
    timecost = end_time - start_time
    print('请求耗时: %.2f秒' % timecost)


if __name__ == '__main__':
    sync_vivogpt()