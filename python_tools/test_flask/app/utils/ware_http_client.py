import http.client
import json
from app.routes.ware_routes import HOST,TOKEN,URL,SHOP_LIST_JSON
from app.common.sign import METHOD
class APIClient:
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
class BizParams:
    DEFAULT_VALUES = SHOP_LIST_JSON

    def __init__(self, data=None):
        if data is None:
            data = {}
        for key, default_value in SHOP_LIST_JSON.items():
            setattr(self, key, data.get(key, default_value))

    def to_json(self):
        body = json.dumps(self.__dict__, ensure_ascii=False, indent=4)
        return json.loads(body)

    def update_params(self, **kwargs):
        for param, value in kwargs.items():
            if param in SHOP_LIST_JSON:
                setattr(self, param, value)
            else:
                print(f"Parameter {param} does not exist.")
# Example usage
json_data = SHOP_LIST_JSON
params = BizParams(json_data)
