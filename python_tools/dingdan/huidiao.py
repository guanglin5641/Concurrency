import requests
import json

def huidiao(created_at):
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
   "biz_content": f'{{\n    \"id\": 3218,\n    \"created_at\": \"2024-01-26 17:31:10\",\n    \"updated_at\": \"{created_at}\",\n    \"ori_id\": 20444,\n    \"ori_order\": \"{{\\\"title\\\":\\\"荷包蛋\\\",\\\"pic_url\\\":\\\"https://img.alicdn.com/i4/10000000003767/O1CN014cDSt31dhKZNTKew6_!!10000000003767-0-koubei.jpg\\\",\\\"shop_name\\\":\\\"正宗沈氏牛肉汤·牛肉火锅(万科智谷店)\\\",\\\"pay_amount\\\":\\\"28.5\\\",\\\"settle_amount\\\":\\\"0.00\\\",\\\"trace_time\\\":\\\"2024-01-26 17:31:10\\\",\\\"tk_create_time\\\":\\\"2024-01-26 17:31:10\\\",\\\"pay_time\\\":\\\"2024-01-26 17:31:10\\\",\\\"receive_time\\\":\\\"2024-01-26 17:31:10\\\",\\\"settle_time\\\":\\\"2024-01-26 17:31:10\\\",\\\"income\\\":\\\"2.35\\\",\\\"settle\\\":\\\"0.0\\\",\\\"item_id\\\":\\\"7B1E64A1F39BBDF19DE9638DF487CFDB\\\",\\\"product_num\\\":1,\\\"unit_price\\\":\\\"23.2\\\",\\\"category_name\\\":\\\"烧烤\\\",\\\"biz_order_id\\\":8048120139180664250,\\\"parent_order_id\\\":8048120139180664250,\\\"main_item_id\\\":\\\"\\\",\\\"main_item_title\\\":\\\"\\\",\\\"order_state\\\":4,\\\"order_item_status_name\\\":\\\"\\\",\\\"settle_state\\\":1,\\\"full_settle_amount\\\":\\\"23.2\\\",\\\"commission_rate\\\":\\\"0.06\\\", \\\"ext_info\\\": \\\"{{\\\\\\\"attrOrderDesc\\\\\\\":\\\\\\\"否\\\\\\\",\\\\\\\"cityName\\\\\\\":\\\\\\\"北京\\\\\\\",\\\\\\\"alscOrderId\\\\\\\":\\\\\\\"8048120139180664250\\\\\\\",\\\\\\\"tpOrderId\\\\\\\":\\\\\\\"8048120139180664250\\\\\\\",\\\\\\\"isSelfPurchase\\\\\\\":\\\\\\\"false\\\\\\\"}}\\\",  \\\"commission_fee\\\":\\\"0.00\\\",\\\"subsidy_rate\\\":\\\"0.0\\\",\\\"subsidy_fee\\\":\\\"0.00\\\",\\\"income_rate\\\":\\\"0.06\\\",\\\"stratify_rate\\\":\\\"\\\",\\\"deduct_rate\\\":\\\"\\\",\\\"platform_commission_rate\\\":\\\"0.0\\\",\\\"platform_commission_fee\\\":\\\"0.00\\\",\\\"channel_rate\\\":\\\"0.0\\\",\\\"channel_fee\\\":\\\"0.0\\\",\\\"media_id\\\":\\\"110001\\\",\\\"media_name\\\":\\\"必应鸟联盟\\\",\\\"ad_zone_id\\\":\\\"5076325\\\",\\\"ad_zone_name\\\":\\\"神犬渠道X\\\",\\\"activity_fee\\\":\\\"0.00\\\",\\\"activity_service_fee\\\":\\\"0.00\\\",\\\"activity_service_rate\\\":\\\"0.0\\\", \\\"order_item_status_name\\\": \\\"\\\", \\\"gmt_modified\\\":\\\"2024-01-26 17:31:10\\\",\\\"tag\\\":\\\"\\\",\\\"sid\\\":\\\"047766602e18bf86ca160c4d2cc53488\\\",\\\"platform_type\\\":2,\\\"activity_id\\\":1358003,\\\"used_store_id\\\":\\\"\\\",\\\"pid\\\":\\\"alsc_12555424_110001_5076325\\\",\\\"relation_order_id\\\":0,\\\"flow_type\\\":3,\\\"order_item_status\\\":4,\\\"activity_info_remark_list\\\":\\\"[]\\\",\\\"channel_right_id\\\":\\\"\\\"}}\",\n    \"client_id\": 2,\n    \"sid\": \"047766602e18bf86ca160c4d2cc53488\",\n    \"supplier_id\": 104,\n    \"order_type\": 1401,\n    \"sub_order_type\": \"3\",\n    \"order_status\": 5,\n    \"parent_order_id\": \"8048120139180664250\",\n    \"sub_order_id\": \"8048120139180664250\",\n    \"item_id\": \"7B1E64A1F39BBDF19DE9638DF487CFDB\",\n    \"item_title\": \"荷包蛋\",\n    \"item_cover\": \"https://img.alicdn.com/i4/10000000003767/O1CN014cDSt31dhKZNTKew6_!!10000000003767-0-koubei.jpg\",\n    \"item_price\": 23.2,\n    \"item_num\": 1,\n    \"order_price\": 23.2,\n    \"pay_price\": 23.2,\n    \"rate\": 0.06,\n    \"pre_commission\": 1.392,\n    \"commission\": 1.392,\n    \"third_service_fee\": 0,\n    \"third_service_ratio\": 0,\n    \"activity_fee\": 0.00,\n    \"activity_service_fee\": 0.00,\n    \"activity_service_ratio\": 0,\n    \"create_time\": \"2024-01-26 17:31:10\",\n    \"pay_time\": \"2024-01-26 17:31:10\",\n    \"receive_time\": \"2024-01-26 17:31:10\",\n    \"union_id\": \"12555424\",\n    \"pid\": \"alsc_12555424_110001_5076325\",\n    \"relation_id\": \"\"\n}}',
   "ext": ""
    }
    )

    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'Host': 'apitest.waimai.biyingniao.com',
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    huidiao("2024-01-26 17:31:10")
