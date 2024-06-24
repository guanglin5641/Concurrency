import http.client
import json
import hashlib
import pymysql
import schedule
import time

def shop_list(leimu) :
    host = "apitest.waimai.biyingniao.com"
    url = "/mobile/bwc/local_elm_shop_list"
    port = 443

    payload = json.dumps({
    "page_index": "",
    "page_size": 20,
    "sort_type": "distance",
    "in_activity": False,
    "filter_type": 1,
    "latitude": 30.28019,
    "longitude": 120.020485,
    "invite_code": "AA8A344",
    "one_point_five_categories": f"{leimu}"
})

    headers = {
        'User-Agent' : 'Apifox/1.0.0 (https://apifox.com)' ,
        'Content-Type' : 'application/json' ,
        'Accept' : '*/*' ,
        'Host' : host ,
        'Connection' : 'keep-alive'
        }

    conn = http.client.HTTPSConnection(host , port)
    conn.request("POST" , url , payload , headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    conn.close()

    return data
def yibai(payload) :
    conn = http.client.HTTPSConnection("test.warehouse.biyingniao.com")
    headers = {
        'Authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJWYWwiOnsicm9sZV9pZCI6MCwidHlwZSI6MSwidWlkIjoxLCJ1c2VybmFtZSI6IkFkbWluIn0sImV4cCI6MTcxMjYzNDU5NywiaWF0IjoxNzEyNjI3Mzk3LCJuYmYiOjE3MTI2MjczOTd9.9r1fdbT4M_avKu28XRLQYvw5-MWZ3VDTqRIh2u7VwTg' ,
        'User-Agent' : 'Apifox/1.0.0 (https://apifox.com)' ,
        'Content-Type' : 'application/json' ,
        'Accept' : '*/*' ,
        'Host' : 'test.warehouse.biyingniao.com' ,
        'Connection' : 'keep-alive' ,
        'Referer' : 'http://test.warehouse.biyingniao.com/api/cps/bwc_shops'
        }
    # 将 payload 转换为 JSON 字符串
    json_payload = json.dumps(payload)
    # 将 JSON 字符串编码为字节
    byte_payload = json_payload.encode('utf-8')

    conn.request("POST" , "/api/cps/bwc_shops" , byte_payload , headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data
def fangfa(index,keyword) :
   body = {
      "biz_type" : "" ,
      "city" : "杭州" ,
      "city_id" : "" ,
      "filter_first_categories" : "" ,
      "filter_has_overlay_coupon" : False ,
      "filter_one_point_five_categories" : "" ,
      "has_bonus_stock" :False  ,
      "in_activity" : True ,
      "include_dynamic" : True ,
      "keyword" : f"{keyword}" ,
      "lat" : 30.280188 ,
      "lng" : 120.020485 ,
      "media_activity_id" : "" ,
      "min_commission_rate" : 0 ,
      "min_overlay_coupon_amount" : 0 ,
      "page_index" : f"{index}" ,
      "page_size" : 20 ,
      "pid" : "alsc_12555424_110001_18470109" ,
      "recall_overlay_coupon" : True ,
      "shop_id" : "" ,
      "sid" : "9a80e5f0a41585649098f03da0d150e5" ,
      "sort" : "distance" ,
      "union_id" : ""
      }

   key = 'bdapba'
   secret = 'c2b7efd73fbad150a4d51c5b6bf71172'

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
   # print(encoded_params)
   string_sign_temp = encoded_params + secret  # 拼接参数签名
   # 计算MD5散列值
   sign = hashlib.md5(string_sign_temp.encode()).hexdigest()
   # print(sign)
   param['sign'] = sign
   # print(param)
   return param
def shop_db(sql) :
   # Connect to the database

   db = pymysql.connect(
      host="rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com" ,
      user="taomama" ,
      password="!qazxsw2" ,
      database="shenquan" ,
      port=3306
      )
   cursor = db.cursor()
   cursor.execute(sql)
   res = cursor.fetchall()
   db.close()
   return res
def yunxing(shop_name):
    index = ""
    while True :
        shop_list_data = yibai(fangfa(index,shop_name))  # 假设 yibai 和 fangfa 已定义
        shop_list_json = json.loads(shop_list_data)
        shop_list_index = shop_list_json["data"]['page_index']
        shop_list_requst = shop_list_json['request_id']
        shop_lists = shop_list_json["data"]['data']
        stop = False  # 控制跳出while循环的标志
        len_num = len(shop_lists)
        for shop_list in shop_lists :
            act = shop_list['activity']
            act_num = act['daily_rest_stock']
            # print(f'订单数{act_num}')
            if act_num == 0 :
                name = shop_list['shop_name']
                request_id = shop_list_requst
                print(name)
                # return name,request_id
        if len_num < 20 :
            break  # 跳出while循环
        index = shop_list_index  # 正确地增加index
    # name = "未查询到"
    # request_id = shop_list_requst
    # return name,request_id
def job():
    name,index = yunxing()
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"运行时间:{now}，获取店铺:{name}，序号:{index}")



if __name__ == '__main__':
    # 安排任务在每分钟执行一次
    # schedule.every(1).minutes.do(job)
    # while True:
    #     schedule.run_pending()
    #     # time.sleep(1)
    keyword="店"
    yunxing(keyword)
