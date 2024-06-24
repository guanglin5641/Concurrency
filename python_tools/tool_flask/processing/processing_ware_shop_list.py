import json
from tool_flask.interface.ware_interface import INTER
from tool_flask.json_data.ware_shop_list_json import params
def select_zero_inventory(shop_name) :
    results = []
    index = ""
    while True :
        params.update_params(keyword=shop_name , page_index=index)
        body = params.to_json()
        jiekou = INTER(body)
        shop_list_data = jiekou.shop_list()
        shop_list_json = json.loads(shop_list_data)
        shop_list_index = shop_list_json["data"]['page_index']
        shop_list_request = shop_list_json['request_id']
        shop_lists = shop_list_json["data"]['data']
        len_num = len(shop_lists)

        for shop_list in shop_lists :
            act = shop_list['activity']
            act_num = act['daily_rest_stock']
            if act_num == 0 :
                name = shop_list['shop_name']
                results.append({
                    "shop_name" : name ,
                    "daily_rest_stock" : act_num ,
                    "request_id" : shop_list_request
                    })

        if len_num < 20 :
            break  # 跳出while循环
        index = shop_list_index  # 正确地增加index
    return results
def shop_list_one_hundred(lat,lng):
    lat = float(lat)
    lng = float(lng)
    params.update_params(include_dynamic=False,page_size=100,lat=lat,lng=lng)
    body= params.to_json()
    jiekou=INTER(body)
    print(body)
    return (jiekou.shop_list())
if __name__ == '__main__':
    a = shop_list_one_hundred(30.280188,120.020485)
    print(a)
