#!/usr/bin/env python
# encoding: utf-8


import random
import string
import time
import hashlib
import hmac
import base64
import urllib.parse

__all__ = ['gen_sign_headers']
'''所有项目中的文件中导入gen_sign_headers,from 项目文件中 
 import gen_sign_headers'''

# 随机字符串
def gen_nonce(length=8):#指定生成参数length=8.的函数
    '''名为char的字符串由小写字母和数字组成
    string.ascii_lowercase包含了所有的小写英文字母（a-z），
    而string.digits包含了所有的数字（0-9）'''
    chars = string.ascii_lowercase + string.digits
    #返回生成的列表中所有的字符连接成一个字符串，从chars中随机取length个字符
    return ''.join([random.choice(chars) for _ in range(length)])


# 如果query项只有key没有value时，转换成params[key] = ''传入
def gen_canonical_query_string(params):#函数，参数
    if params:#参数不为空 
        #导入urllib.parse.quote函数并将其赋值给escape_uri变量。
        #这个函数用于对URL中的特殊字符进行转义
        escape_uri = urllib.parse.quote 
        raw = [] #列表

        
        for k in sorted(params.keys()):
            #这段代码的目的是创建一个新的列表 raw，其中包含 params 字典中的所有键值对
            if params[k] == '':
                raw.append((k, ''))
            else:
                raw.append((k, params[k]))
            #调用escape_uri 的函数，作用通常是对传入的字符串进行 URI 编码
            #以确保它可以在 URI 中安全使用。params 的字典中获取键为 k 的值
            #并将其转换成字符串形式，再次调用 escape_uri 函数对这个字符串进行 URI 编码。
            #创建了一个元组 tmp_tuple，其中第一个元素是 k 的 URI 编码，第二个元素是 params[k] 的 URI 编码。
            tmp_tuple = (escape_uri(k), escape_uri(str(params[k])))
            #创建了一个元组，其中包含了两个 URI 编码的字符串，一个是键 k，另一个是 params 字典中对应于 k 的值。
            
            #将tmp_tuple添加到raw列表中。
            raw.append(tmp_tuple)
        s = "&".join("=".join(kv) for kv in raw)#k=v&k=v....
        return s
    else: #参数为空
        return ''

#生成签名
def gen_signature(app_secret, signing_string):#密钥，签名字符串
    #app_secret（一个字符串）编码为UTF-8格式的字节串。这是因为HMAC
    #（Hash-based Message Authentication Code）函数需要一个字节串作为密钥。
    bytes_secret = app_secret.encode('utf-8') 

    #创建了一个新的HMAC对象。它使用SHA-256作为底层哈希函数，
    #bytes_secret 作为密钥，signing_string 作为要签名的消息。
    hash_obj = hmac.new(bytes_secret, signing_string, hashlib.sha256)

    #调用 hash_obj.digest() 来获取HMAC的原始字节表示。
    #使用base64编码来将这些字节转换为一个可打印的字符串，
    #这通常更容易在文本协议中传输。
    bytes_sig = base64.b64encode(hash_obj.digest())

    #将base64编码的字节串转换为UTF-8编码的字符串
    signature = str(bytes_sig, encoding='utf-8')
    return signature

#这就是__all__ = ['gen_sign_headers']
def gen_sign_headers(app_id, app_key, method, uri, query):
    method = str(method).upper()#将方法名（如GET、POST等）转换为大写
    uri = uri
    #使用time.time()获取当前时间的时间戳（以秒为单位），然后将其转换为字符串。
    timestamp = str(int(time.time()))
    app_id = app_id
    app_key = app_key
    nonce = gen_nonce()#随机字符串
    #如果query项只有key没有value时，转换成params[key] = ''传入
    canonical_query_string = gen_canonical_query_string(query)
    #使用format方法将app_id、timestamp和nonce插入到字符串中，生成一个签名头部字符串
    signed_headers_string = 'x-ai-gateway-app-id:{}\nx-ai-gateway-timestamp:{}\n' \
                            'x-ai-gateway-nonce:{}'.format(app_id, timestamp, nonce)
    
    #用format方法将上述的所有组件拼接成一个签名字符串。
    signing_string = '{}\n{}\n{}\n{}\n{}\n{}'.format(method,
                                                     uri,
                                                     canonical_query_string,
                                                     app_id,
                                                     timestamp,
                                                     signed_headers_string)
    signing_string = signing_string.encode('utf-8') #编码为UTF-8格式
    signature = gen_signature(app_key, signing_string)
    return {
        'X-AI-GATEWAY-APP-ID': app_id,
        'X-AI-GATEWAY-TIMESTAMP': timestamp,
        'X-AI-GATEWAY-NONCE': nonce,
        'X-AI-GATEWAY-SIGNED-HEADERS': "x-ai-gateway-app-id;x-ai-gateway-timestamp;x-ai-gateway-nonce",
        'X-AI-GATEWAY-SIGNATURE': signature
    }