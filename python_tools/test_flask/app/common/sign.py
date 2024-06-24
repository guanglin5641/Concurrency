import json
import time
import hashlib
from app.routes.ware_routes import KEY,SECRET
class METHOD:
   def __init__(self,body):
      self.body = body
   def sign_method(self) :
      body = self.body
      key = KEY
      secret = SECRET
      param = {
         'app_key' : key ,
         'timestamp' : int(time.time()) ,
         'version' : '1.0' ,
         'format' : 'json' ,
         'charset' : 'utf-8' ,
         'sign_type' : 'md5' ,
         'biz_content' : '' ,
         'ext' : ''
         }
      if body is not None :
         json_data = json.dumps(body)
         param['biz_content'] = json_data
      keys = [key for key in param if key != 'sign']
      keys.sort()
      param_pairs = []
      for k in keys :
         if k == 'ext' and param[k] == '' :
            continue
         param_pairs.append(f"{k}={param[k]}")
      encoded_params = '&'.join(param_pairs)
      string_sign_temp = encoded_params + secret  # 拼接参数签名
      # 计算MD5散列值
      sign = hashlib.md5(string_sign_temp.encode()).hexdigest()
      param['sign'] = sign
      return param
