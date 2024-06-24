import json
import hashlib
import time
import http.client

def generate_sign(param, secret):
    param_str = ''
    keys = sorted(param.keys())
    for key in keys:
        if key != 'sign':
            if key == 'biz_content':
                param_str += key + '=' + json.dumps(param[key], separators=(',', ':')) + '&'
            else:
                param_str += key + '=' + str(param[key]) + '&'
    param_str = param_str[:-1]  # Remove the last '&'
    param_str += secret
    print(1,param_str)
    sign = hashlib.md5(param_str.encode()).hexdigest()
    return sign

def main():
    # 替换为你的请求 URL
    host = "qyb.biyingniao.com"
    url = "/api/notice/send/tpl"
    # 替换为你的密钥
    key = "medbxd"
    secret = "1592f9e19aa0e707b8e18ac34827f3d9"

    # 获取当前时间戳
    timestamp = int(time.time())

    # 替换为你的请求体参数
    payload = {
        "template_id" : "d5d71c97e7cbbcc84d7162e23d8da4ad" ,
        "client_user_id" : 769585595 ,
        "param_map" : "{\"client_user_id\":\"769585595\"}" ,
        "third_msg_id" : "AAABBACCAA" ,
        "is_sync" : True ,
        "event_rule_type" : 1
}

    # 构建签名所需参数
    param = {
        'app_key': key,
        'timestamp': timestamp,
        'version': '1.0',
        'format': 'json',
        'charset': 'utf-8',
        'sign_type': 'md5',
        'biz_content': payload,
        'ext': ''
    }
    # 生成签名
    param['sign'] = generate_sign(param, secret)
    # 构建请求体
    body = json.dumps(param)
    print(2,generate_sign(param, secret))
    print(3,body)

    # 构建请求头
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': host,
        'Connection': 'keep-alive'
    }
    #发起请求
    conn = http.client.HTTPSConnection(host)
    conn.request("POST", url, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data.decode("utf-8"))
    conn.close()

if __name__ == "__main__":
    main()