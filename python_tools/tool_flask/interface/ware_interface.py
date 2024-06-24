import http.client
import json
from tool_flask.common.sign import METHOD
from tool_flask.common.constant import HOST,TOKEN,URL
from tool_flask.json_data.ware_shop_list_json import params

class INTER:
    def __init__(self,body,prot:str = "http",host:str = HOST,token:str = TOKEN,url:str = URL):
        self.body = body
        self.prot = prot
        self.host = host
        self.token = token
        self.url = url
    def shop_list(self) :
        method = METHOD(self.body)
        print(self.body)
        payload = method.sign_method()
        print(payload)
        conn = http.client.HTTPSConnection(self.host)
        headers = {
            'Authorization' : self.token,
            'Content-Type' : 'application/json' ,
            'Accept' : '*/*' ,
            'Host' : self.host ,
            'Connection' : 'keep-alive' ,
            'Referer' : f'{self.prot}:{self.host}{self.url}'
            }
        # 将 payload 转换为 JSON 字符串
        json_payload = json.dumps(payload)
        # 将 JSON 字符串编码为字节
        byte_payload = json_payload.encode('utf-8')

        conn.request("POST" , self.url , byte_payload , headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return data
if __name__ == '__main__':
    body = params.to_json()
    inter = INTER(body)
    inter.shop_list()