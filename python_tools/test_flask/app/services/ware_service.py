import json
from app.utils.ware_http_client import APIClient
from app.utils.ware_http_client import BizParams
from app.routes.ware_routes import SHOP_LIST_JSON,HOST,TOKEN,URL
body = BizParams(SHOP_LIST_JSON)


def select_zero_inventory(shop_name):

    results = []
    index = ""
    while True:
        body.update_params(keyword=shop_name, page_index=index)
        body_json = body.to_json()
        jiekou = APIClient(body_json)
        shop_list_data = jiekou.shop_list()
        shop_list_json = json.loads(shop_list_data)
        # print(shop_list_json)
        shop_list_index = shop_list_json["data"]['page_index']
        shop_list_request = shop_list_json['request_id']
        shop_lists = shop_list_json["data"]['data']
        len_num = len(shop_lists)
        for shop_list in shop_lists:
            act = shop_list['activity']
            act_num = act['daily_rest_stock']
            if act_num == 0:
                name = shop_list['shop_name']
                results.append({
                    "shop_name": name,
                    "daily_rest_stock": act_num,
                    "request_id": shop_list_request
                })

        if len_num < 20:
            break  # 跳出while循环
        index = shop_list_index  # 正确地增加index
    return results

def shop_list_one_hundred(lat, lng):
    lat = float(lat)
    lng = float(lng)
    body.update_params(include_dynamic=False, page_size=100, lat=lat, lng=lng)
    parmas = body.to_json()
    jiekou = APIClient(HOST, TOKEN, URL,parmas)
    data = jiekou.call_api()
    return data.shop_list()
if __name__ == '__main__':
    a = '店'
    # select_zero_inventory(a)
    print(select_zero_inventory(a))