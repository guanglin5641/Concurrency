import json
import random
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import requests

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = "LVMaGmqFCHyERJmA"

iox = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_AL_3_198591435",
    "threadId": "R_AL_3_198591435"
}

data = json.dumps(iox)

# 生成指定长度的随机字符串
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# 获取固定的加密密钥
def get_encSecKey():
    return "1355bfd8ba249ea0747cf0d54e79db6d813c2e61d2f751285fc794d0692f7d56e67e491c3b8d136a1952bd7fbdc185bd91fe4fd077d5dd27dd22ae11267a9d12980b5f403d9d6c2e91e217150983aab4081278dba41b42e4e20431b6f9190de3f343b625db5ccc27529cd708bd77ce3ad5d09a0d6c589fed383d9cf055f88d80"

# 使用AES对数据进行加密
def aes_encrypt(data, key):
    IV='0102030405060708'
    cipher = AES.new(key.encode('utf-8'),  IV=IV.encode('utf-8'),mode= AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')

# 综合使用以上方法对数据进行加密
def get_encrypted_data(data, g):

    first_encrypted = aes_encrypt(data, g)  # 使用g作为密钥和IV进行第一次AES加密
    enc_text = aes_encrypt(first_encrypted, i)  # 使用g作为密钥，i作为IV进行第二次AES加密
    return enc_text

# 发送 POST 请求
response = requests.post(url, data={
    'params': get_encrypted_data(data, g),
    'encSecKey': get_encSecKey()
})

# 打印响应
print(response.text)
