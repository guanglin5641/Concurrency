import json
import common.mysql
import connector.store_list
import common.Email
import connector.list_redis

def run_shop_list():
    db = common.mysql.DB()
    sql_ku = 'etuantuan'
    sql = """select 
    bs.store_name ,bsp.longitude,bsp.latitude,bsp.id 
    from 
    {0}.bwc_store_promotion bsp 
    join 
    {0}.bwc_store bs 
    on 
    bs.id = bsp.store_id  
    where 
    promotion_end_date >= CURDATE() 
    and 
    promotion_start_date <= CURDATE() 
    and 
    promotion_status = 2;""".format(sql_ku, sql_ku)
    # print(sql)
    data_list = db.select(sql)
    a = len(data_list)
    mes = []
    for i in range(a):
        store_name = data_list[i]["store_name"].strip()
        longitude = data_list[i]["longitude"]
        latitude = data_list[i]["latitude"]
        promotion_id = data_list[i]["id"]
        data = connector.store_list.get_list_promotions(longitude, latitude, store_name)
        # print("data:", data)

        data_dict = json.loads(data)
        # print(data)
        if data_dict["data"]["list"] is not None:
            store_names = [item["store"]["store_name"] for item in data_dict["data"]["list"]]
            if store_name not in store_names:
                mes.append(store_name +promotion_id+ "未查询到")
                # print(promotion_id)
                # print(connector.list_redis.redis_link(promotion_id))

        else:
            mes.append(store_name +promotion_id+ "未查询到")
            # print(promotion_id)
            # print(connector.list_redis.redis_link(promotion_id))
    # print(mes)
    if not mes:
        # print("查询结束,无错误店铺")
        common.Email.E_mail("查询结束,无错误店铺")
    else:
        mes_str = "\n".join(mes)  # 将列表元素连接成字符串
        # print("查询结束\n" + mes_str)
        common.Email.E_mail("查询结束\n" + mes_str)
    return ()

if __name__ == '__main__':
    run_shop_list()