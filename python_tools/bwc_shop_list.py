import requests
import json
import pymysql
import csv
import http.client
import json

def write_to_csv(data , filename) :
    """
    将数据写入CSV文件

    参数：
    data: 包含数据的列表套列表或列表套字典
    filename: 要写入的CSV文件名

    返回：
    无
    """
    # 确定数据是否为字典列表
    is_dict_data = isinstance(data[0] , dict)

    # 写入数据到CSV文件
    try :
        with open(filename , 'w' , newline='' , encoding='utf-8') as csvfile :
            if is_dict_data :
                # 如果数据是字典列表，则使用DictWriter写入
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile , fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            else :
                # 如果数据是列表套列表，则使用writer写入
                writer = csv.writer(csvfile)
                writer.writerows(data)

        print(f"数据成功写入 {filename}")
    except Exception as e :
        print(f"写入数据到 {filename} 时出错：{e}")




def shop_db():
    # Connect to the database
    db = pymysql.connect(host="rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com" ,
                         user="taomama" ,
                         password="!qazxsw2" ,
                         database="shenquan" ,
                         port=3306)
    # if a == 1:
    try :
        with db.cursor() as cursor :
            # Execute SQL query to fetch data
            sql = "SELECT ext FROM shenquan_dev.client_user cu WHERE ext IS NOT NULL limit 10   ;"
            cursor.execute(sql)
            res = cursor.fetchall()

            # Process the query results
            shop_list = []
            for row in res :
                data = json.loads(row[0])  # Parse JSON string
                shop_list.append(data)

            return shop_list

    finally :
        db.close()
    # else:
    #     sql = "SELECT ext FROM shenquan.client_user cu WHERE ext IS NOT NULL;"
    #     cursor.execute(sql)
    #     res = cursor.fetchall()





def shop_list(lat , long) :
    host = "apitest.waimai.biyingniao.com"
    url = "/mobile/bwc/local_elm_shop_list"
    port = 443

    payload = json.dumps({
        "page_index" : "" ,
        "page_size" : 20 ,
        "sort_type" : "normal" ,
        "in_activity" : False ,
        "filter_type" : 1 ,
        "latitude" : lat ,
        "longitude" : long ,
        "one_point_five_categories" : ""
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


if __name__ == '__main__':
    csv_data = []
    # 将打印结果组成适合写入CSV的格式
    shop_list_ls = shop_db()
    for i in shop_list_ls :
        lat = i["workplace_lat"]
        long = i["workplace_lng"]
        name = i["workplace_addr"]

        a_text = shop_list(lat , long)
        # print(a_text)
        data_json = json.loads(a_text).get("data" , { }).get("data")  # 使用get方法避免可能的键错误
        # data_data = a_text.json()["data"]["request_id"]
        if data_json is not None :
            for shop_info in data_json :
                print(name , shop_info["shop_name"] , shop_info["activity"]["pre_amount"],json.loads(a_text)["request_id"],a_text if shop_info["activity"]["pre_amount"] == 0 else "",lat,long)
                # 组成字典
                #奖励金门槛
                bounty_min_limit_cent = shop_info["activity"]["bounty_min_limit_cent"]
                #奖励红包金额
                bonus_amount = shop_info["activity"]["bonus_amount"]
                #起送价
                delivery_fee = shop_info["extend"]["delivery_min_price"]
                # #判断
                # if delivery_fee <= 20:
                #     if bounty_min_limit_cent <= 10:
                #         if bonus_amount < 6:
                #             #客单价=8.9
                #             Customer_price = 8.9
                csv_data.append({
                    "商圈区域" : name ,
                    "店铺名" : shop_info["shop_name"] ,
                    "客单价显示金额" : shop_info["activity"]["pre_amount"],
                    "request_id" : json.loads(a_text)["request_id"],  # 同样使用get方法
                    "error" :shop_info ,#if shop_info["activity"]["pre_amount"] == 0 else "" , # 根据pre_amount是否为零来确定错误信息
                    "lat":lat,
                    "long":long,
                    "奖励金门槛" : bounty_min_limit_cent ,
                    "奖励红包金额" : bonus_amount ,
                    "起送价" : delivery_fee
                    })
        else :
            print(f"数据为空：{name}")
    filename = r'C:\Users\lenovo\Desktop\aaaa.csv'
    # 使用列表套列表的数据
    write_to_csv(csv_data , filename)
