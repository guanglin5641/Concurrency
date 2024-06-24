# utils.py
import time
import pymysql
import requests
import json
from collections import defaultdict

class jiekou:
    def __init__(self):
        self.lat = 30.284519
        self.lng = 120.025794
        self.host = "api.waimai.biyingniao.com"
        self.token = 'your_token_here'
        self.open_user = '38881928'
        self.S_City = '330100'

    def user_mark(self):
        url = f"http://{self.host}/mobile/user/mark_business_district"
        payload = json.dumps({"lat": self.lat, "lng": self.lng})
        headers = {
            'S-Open-User': self.open_user,
            'S-Platform': 'h5',
            'S-Ip': '192.168.101.45',
            'S-Version': '1.124',
            'S-City': self.S_City,
            'S-Trace-Id': '11',
            'S-Time': '1223',
            'S-Token': self.token,
            'S-Login-User': '75608a12ecdbef708edba49eeef2e9cd',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': self.host,
            'Connection': 'keep-alive'
        }
        requests.post(url, headers=headers, data=payload)

    def request(self, index):
        url = f"http://{self.host}/mobile/bwc/local_elm_shop_list"
        payload = json.dumps({
            "latitude": self.lat,
            "longitude": self.lng,
            "page_index": str(index),
            "page_size": 100,
            "in_activity": False,
            "filter_type": 1,
            "sort_type": "normal",
            "one_point_five_categories": ""
        })
        S_time = int(time.time())
        headers = {
            'S-Open-User': self.open_user,
            'S-Platform': 'h5',
            'S-Version': '1.0.0',
            'S-City': self.S_City,
            'S-Trace-Id': '11',
            'S-Time': str(S_time),
            'S-Token': self.token,
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': self.host,
            'Connection': 'keep-alive'
        }
        response = requests.post(url, headers=headers, data=payload)
        return response

    def count_shops_by_district(self, shop_data):
        district_counts = defaultdict(int)
        for shop_info in shop_data:
            district = list(shop_info.values())[0]
            district_counts[district] += 1
        return district_counts

def shop_db(shop_name):
    db = pymysql.connect(host="rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com", user="taomama", password="!qazxsw2", database="shenquan", port=3306)
    try:
        with db.cursor() as cursor:
            sql = f"SELECT shop_name, business_district FROM shop_reports WHERE shop_name = '{shop_name}' GROUP BY shop_name;"
            cursor.execute(sql)
            res = cursor.fetchall()
            result_dict = {row[0]: row[1] for row in res} if res else {}
            return result_dict
    finally:
        db.close()

def convert_to_meters(distance_str):
    if 'km' in distance_str:
        return float(distance_str.replace('km', '')) * 1000
    elif 'm' in distance_str:
        return float(distance_str.replace('m', ''))
    else:
        return 10000

def fangfa():
    jk = jiekou()
    index = ""
    res_list = []
    res_all_list = []
    dis_all_list = []
    count = 0
    count_a = 0

    while count < 2:
        response = jk.request(index)
        res_json = response.json()["data"]["data"]

        if res_json is not None:
            for i in res_json:
                res_all_list.append(i["shop_name"])
                dis_all_list.append(i["distance"])
                if convert_to_meters(i["distance"]) <= 3000:
                    res_list.append(i["shop_name"])
        index = response.json()["data"]["page_index"]
        count += 1

    c = 0
    d = 0
    business_district = []
    for i in res_list:
        count_a += 1
        if shop_db(i) == {}:
            c += 1
        else:
            d += 1
            business_district.append(shop_db(i))
    a = jk.count_shops_by_district(business_district)
    for district, count in a.items():
        print(f"商业区 '{district}' 中有 {count} 个店铺。")
    print(f"有商圈的为：{d}无商圈的为：{c}")
    return d, c
