import http.client
import json
from app.routes.shenqun_routes import HOST,TOKEN,ORDER_CALL_BACKS_URL,ORDER_CALL_BACKS_JSON
from app.common.sign import METHOD
import time
import re
from datetime import datetime
class APIClient:
    def __init__(self,body,prot:str = "http",host:str = HOST,token:str = TOKEN,url:str = ORDER_CALL_BACKS_URL):
        self.body = body
        self.prot = prot
        self.host = host
        self.token = token
        self.url = url
    def order_call_backs(self) :
        payload = self.body
        conn = http.client.HTTPSConnection(self.host)
        headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json',
   'Accept': '*/*',
   'Host': f'{self.host}',
   'Connection': 'keep-alive'
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
    def __init__(self, data=None):
        if data is None:
            data = ORDER_CALL_BACKS_JSON
        self.data = data

    def to_json(self):
        return json.loads(json.dumps(self.data, ensure_ascii=False, indent=4))

    def update_params(self, **kwargs):
        self._recursive_update(self.data, kwargs)

    def _recursive_update(self, json_obj, update_dict):
        if isinstance(json_obj, dict):
            for key, value in json_obj.items():
                if isinstance(value, str):
                    value = self._replace_placeholders(value, update_dict)
                    json_obj[key] = value
                    # 尝试将字符串解析为 JSON 对象并递归更新
                    if re.match(r'^\{.*\}$', value) or re.match(r'^\[.*\]$', value):
                        try:
                            nested_json = json.loads(value)
                            self._recursive_update(nested_json, update_dict)
                            json_obj[key] = json.dumps(nested_json)
                        except json.JSONDecodeError:
                            pass
                elif isinstance(value, (dict, list)):
                    self._recursive_update(value, update_dict)
        elif isinstance(json_obj, list):
            for i, item in enumerate(json_obj):
                if isinstance(item, str):
                    item = self._replace_placeholders(item, update_dict)
                    json_obj[i] = item
                    # 尝试将字符串解析为 JSON 对象并递归更新
                    if re.match(r'^\{.*\}$', item) or re.match(r'^\[.*\]$', item):
                        try:
                            nested_json = json.loads(item)
                            self._recursive_update(nested_json, update_dict)
                            json_obj[i] = json.dumps(nested_json)
                        except json.JSONDecodeError:
                            pass
                else:
                    self._recursive_update(item, update_dict)

    def _replace_placeholders(self, text, update_dict):
        for placeholder, value in update_dict.items():
            text = text.replace(f"${{{placeholder}}}", str(value))
        return text


# 示例用法
json_data = ORDER_CALL_BACKS_JSON
params = BizParams(json_data)
