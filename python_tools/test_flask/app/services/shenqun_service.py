from app.utils.shenquan_http_client import APIClient, BizParams
import time
from datetime import datetime
from app.routes.shenqun_routes import TEST_MYSQL,ORDER_CALL_BACKS_JSON
from app.common.mysql import MysqlHelper

# 获取当前时间并格式化
datetime_obj = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")

def read_order_no():
    db_test = MysqlHelper(TEST_MYSQL)
    sql = '''SELECT order_no FROM shenquan_dev.collect_order co ORDER BY order_no DESC LIMIT 1'''
    params = ()
    order_no = int(db_test.get_one(sql, params)[0]) + 1
    return order_no

def bwc_order(
        order_no: str = None,
        shop_name: str = "测试店铺",
        order_time: str = None,
        price: str = "35.5",
        order_state: str = "4",
        name: str = "",
        open_user_id: str = "129",
        order_type: str = "1",
        is_cycle: str = "0",
        cycle_num: str = "0"
    ):
    # 转换 cycle_num 为整数
    cycle_num = int(cycle_num)

    if order_no is None:
        order_no = read_order_no()
    if order_time is None:
        order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def sid_create(open_user_id: str):
        sql = f'''
        SELECT pt.keyword FROM shenquan_dev.open_user ou 
        JOIN shenquan_dev.client_user cu ON ou.id = cu.open_user_id 
        JOIN shenquan_dev.promotion_tracks pt ON cu.client_user_id = pt.client_user_id 
        WHERE ou.id = {open_user_id} GROUP BY pt.keyword LIMIT 1;
        '''
        params = ()
        num = MysqlHelper(TEST_MYSQL).get_one(sql, params)
        sid = "ca1e4f5b2226b133852e6484c48d00cc" if num is None else num[0]
        return sid

    sid = sid_create(open_user_id)

    # 初始化 response
    response = {'data': []}

    # 确保 is_cycle 仅为 0 或 1
    is_cycle = int(is_cycle) if is_cycle in ["0", "1"] else 0
    print(is_cycle)
    if is_cycle == 0:
        json_data = ORDER_CALL_BACKS_JSON
        params = BizParams(json_data)
        params.update_params(
            order_no=order_no,
            time=order_time,
            shop_name=shop_name,
            price=price,
            order_state=order_state if order_state not in [0, 1, 2, 3, 4, 5, 6] else 4,
            name=name,
            sid=sid,
            order_type=order_type if order_type not in [1400, 1401, 1402, 1405] else 1401
        )

        body = params.to_json()
        api = APIClient(body)
        data = api.order_call_backs()
        response['data'].append({"data": data, "order_no": order_no})
    else :

        order_list = [read_order_no() + i for i in range(cycle_num)]
        for order_no in order_list :
            json_data = ORDER_CALL_BACKS_JSON
            params = BizParams(json_data)
            params.update_params(
                order_no=order_no ,
                time=order_time ,
                shop_name=shop_name ,
                price=price ,
                order_state=order_state if order_state not in [0 , 1 , 2 , 3 , 4 , 5 , 6] else 4 ,
                name=name ,
                sid=sid ,
                order_type=order_type if order_type not in [1400 , 1401 , 1402 , 1405] else 1401
                )
            json_data = ORDER_CALL_BACKS_JSON
            params = BizParams(json_data)
            print(f"Order No: {order_no}")
            print(f"Params: {params.to_json()}")

            body = params.to_json()
            # api = APIClient(body)
            # print(body)
            # data = api.order_call_backs()
            # response['data'].append({ "data" : data , "order_no" : order_no })
            # time.sleep(0.2)

    return response

