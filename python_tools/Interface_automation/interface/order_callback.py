import requests
import json
import time
from datetime import datetime


class HuiDIao:
    def __init__(
            self,
            pid,
            order_no,
            sid,
            category_name,
            activity_id,
            out_subsidy_fee,
            out_commission_fee ,
            out_platform_commission_fee,
            out_activity_fee,
            out_activity_service_fee,
            city_name: str = "杭州",
            pay_amount: int = 28.5,
            settle_amount: int = 29.8,
            order_state: int = 4

    ):
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.pid = pid
        self.order_no = order_no
        self.pay_amount = pay_amount
        self.settle_amount = settle_amount
        self.order_state = order_state
        self.sid = sid
        self.city_name = city_name
        self.category_name = category_name
        self.activity_id = activity_id
        self.out_subsidy_fee = out_subsidy_fee
        self.out_commission_fee = out_commission_fee
        self.out_platform_commission_fee = out_platform_commission_fee
        self.out_activity_fee = out_activity_fee
        self.out_activity_service_fee = out_activity_service_fee
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'Host': 'apitest.waimai.biyingniao.com',
            'Connection': 'keep-alive'
        }
    def huidiao(self):
        url = "http://apitest.waimai.biyingniao.com/api/order/save"
        payload = json.dumps(
            {
                "app_key": "",
                "timestamp": 1,
                "version": "1.0",
                "format": "",
                "charset": "",
                "sign_type": "",
                "sign": "",
                "biz_content": f'{{\
       "id": 3218,\
       "created_at": "{self.time}",\
       "updated_at": "{self.time}",\
       "ori_id": 20444,\
       "ori_order": "{{\
           \\"title\\":\\"荷包蛋\\",\
           \\"pic_url\\":\\"https://img.alicdn.com/i4/10000000003767/O1CN014cDSt31dhKZNTKew6_!!10000000003767-0-koubei.jpg\\",\
           \\"shop_name\\":\\"正宗沈氏牛肉汤·牛肉火锅(万科智谷店)\\",\
           \\"pay_amount\\":\\"{self.pay_amount}\\",\
           \\"settle_amount\\":\\"0.00\\",\
           \\"trace_time\\":\\"{self.time}\\",\
           \\"tk_create_time\\":\\"{self.time}\\",\
           \\"pay_time\\":\\"{self.time}\\",\
           \\"receive_time\\":\\"{self.time}\\",\
           \\"settle_time\\":\\"{self.time}\\",\
           \\"income\\":\\"2.35\\",\
           \\"settle\\":\\"0.0\\",\
           \\"item_id\\":\\"7B1E64A1F39BBDF19DE9638DF487CFDB\\",\
           \\"product_num\\":1,\
           \\"unit_price\\":\\"23.2\\",\
           \\"category_name\\":\\"{self.category_name}\\",\
           \\"biz_order_id\\":{self.order_no},\
           \\"parent_order_id\\":{self.order_no},\
           \\"main_item_id\\":\\"\\",\
           \\"main_item_title\\":\\"\\",\
           \\"order_state\\":{self.order_state},\
           \\"order_item_status_name\\":\\"\\",\
           \\"settle_state\\":1,\
           \\"full_settle_amount\\":\\"{self.settle_amount}\\",\
           \\"commission_rate\\":\\"0.06\\",\
           \\"ext_info\\":\\"{{\\\\\\"attrOrderDesc\\\\\\":\\\\\\"否\\\\\\",\\\\\\"cityName\\\\\\":\\\\\\"{self.city_name}\\\\\\",\\\\\\"alscOrderId\\\\\\":\\\\\\"{self.order_no}\\\\\\",\\\\\\"tpOrderId\\\\\\":\\\\\\"{self.order_no}\\\\\\",\\\\\\"isSelfPurchase\\\\\\":\\\\\\"false\\\\\\"}}\\",\
           \\"commission_fee\\":\\"{self.out_subsidy_fee}\\",\
           \\"subsidy_rate\\":\\"0.0\\",\
           \\"subsidy_fee\\":\\"{self.out_subsidy_fee}\\",\
           \\"income_rate\\":\\"0.06\\",\
           \\"stratify_rate\\":\\"\\",\
           \\"deduct_rate\\":\\"\\",\
           \\"platform_commission_rate\\":\\"0.0\\",\
           \\"platform_commission_fee\\":\\"{self.out_platform_commission_fee}\\",\
           \\"channel_rate\\":\\"0.0\\",\
           \\"channel_fee\\":\\"0.0\\",\
           \\"media_id\\":\\"110001\\",\
           \\"media_name\\":\\"必应鸟联盟\\",\
           \\"ad_zone_id\\":\\"5076325\\",\
           \\"ad_zone_name\\":\\"神犬渠道X\\",\
           \\"activity_fee\\":\\"{self.out_activity_fee}\\",\
           \\"activity_service_fee\\":\\"{self.out_activity_service_fee}\\",\
           \\"activity_service_rate\\":\\"0.0\\",\
           \\"order_item_status_name\\":\\"\\",\
           \\"gmt_modified\\":\\"{self.time}\\",\
           \\"tag\\":\\"\\",\
           \\"sid\\":\\"{self.sid}\\",\
           \\"platform_type\\":2,\
           \\"activity_id\\":{self.activity_id},\
           \\"used_store_id\\":\\"\\",\
           \\"pid\\":\\"{self.pid}\\",\
           \\"relation_order_id\\":0,\
           \\"flow_type\\":3,\
           \\"order_item_status\\":{self.order_state},\
           \\"activity_info_remark_list\\":\\"[]\\",\
           \\"channel_right_id\\":\\"\\"\
       }}",\
       "client_id": 2,\
       "sid": "{self.sid}",\
       "supplier_id": 104,\
       "order_type": 1401,\
       "sub_order_type": "3",\
       "order_status": 5,\
       "parent_order_id": "{self.order_no}",\
       "sub_order_id": "{self.order_no}",\
       "item_id": "7B1E64A1F39BBDF19DE9638DF487CFDB",\
       "item_title": "荷包蛋",\
       "item_cover": "https://img.alicdn.com/i4/10000000003767/O1CN014cDSt31dhKZNTKew6_!!10000000003767-0-koubei.jpg",\
       "item_price": 23.2,\
       "item_num": 1,\
       "order_price": 23.2,\
       "pay_price": {self.pay_amount},\
       "rate": 0.06,\
       "pre_commission": 1.392,\
       "commission": 1.392,\
       "third_service_fee": 0,\
       "third_service_ratio": 0,\
       "activity_fee": 0.00,\
       "activity_service_fee": 0.00,\
       "activity_service_ratio": 0,\
       "create_time": "{self.time}",\
       "pay_time": "{self.time}",\
       "receive_time": "{self.time}",\
       "union_id": "12555424",\
       "pid": "{self.pid}",\
       "relation_id": ""\
   }}',
                "ext": ""
            }
        )

        response = requests.request("POST", url, headers=self.headers, data=payload)
        # 打印实际请求
        # print(response.text)
        # 打印实际请求信息
        # print(response.request.body)
        return response.json()


if __name__ == "__main__":
    order = 8048120139180664284
    for i in range(0, 10):
        print("i是" + str(i))
        order += 1
        for y in range(0, 3):
            print("y是" + str(y))
            print(('alsc_12555424_110001_13675021', order))
