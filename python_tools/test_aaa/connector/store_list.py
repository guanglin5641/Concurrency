import http.client
import json
def get_list_promotions(longitude, latitude,store_name):
    conn = http.client.HTTPSConnection("m.eed9.top")
    payload = json.dumps({
        "longitude": longitude,
        "latitude": latitude,
        "page": 1,
        "page_size": 20,
        "promotion_category": 0,
        "promotion_sort": 0,
        "promotion_filter": 0,
        "store_name_filter": store_name
    })
    headers = {
        'S-City': '330100',
        # 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        # 'Host': 'm.eed9.top',
        'Connection': 'keep-alive'
    }
    conn.request("POST", "/mibile/list_promotions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return (data.decode("utf-8"))

if __name__ == '__main__':
    print(get_list_promotions(113.078959,28.183412,'她锅花雕醉鸡(农大店)'))
    # data_dict = json.loads(get_list_promotions(113.078959,28.183412,'她锅花雕醉鸡(农大店)'))
    # store_name= '她锅花雕醉鸡(农大店)'
    # if data_dict["data"]["list"] is not None:
    #     store_names = [item["store"]["store_name"] for item in data_dict["data"]["list"]]
    #     print(store_names)
    #     if store_name not in store_names:
    #         print(store_name + "未查询到")
    # else:
    #         print(store_name + "未查询到")
