# encoding: utf-8
import uuid
import time
import requests

def sync_vivogpt():
    
    
   

    data = {
        'prompt': '大漠孤烟直',
        'model': 'vivo-BlueLM-TB',
        'sessionId': str(uuid.uuid4()),
        'extra': {
            'temperature': 0.9
        }
    }
    return data
