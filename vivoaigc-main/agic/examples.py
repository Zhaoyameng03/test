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
            "content": "这句古诗来自具体那首古诗，用白话文解释一下全文"
        },
        {
            "role": "assistant",
            "content": "请你用第一人称也就是诗人的角度对古诗进行描述，描述的要具体形象并且精炼"
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

