# KEY = 'bdapba'
# SECRET = 'c2b7efd73fbad150a4d51c5b6bf71172'
HOST = 'apitest.waimai.biyingniao.com'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJWYWwiOnsicm9sZV9pZCI6MCwidHlwZSI6MSwidWlkIjoxLCJ1c2VybmFtZSI6IkFkbWluIn0sImV4cCI6MTcxMjYzNDU5NywiaWF0IjoxNzEyNjI3Mzk3LCJuYmYiOjE3MTI2MjczOTd9.9r1fdbT4M_avKu28XRLQYvw5-MWZ3VDTqRIh2u7VwTg'
ORDER_CALL_BACKS_URL = "/api/order/save"
ORDER_CALL_BACKS_JSON = {
    "app_key": "",
    "timestamp":1,
    "version":"1.0",
    "format":"",
    "charset":"",
    "sign_type":"",
    "sign":"",
    "biz_content":"{\"id\":1284900,\"created_at\":\"${time}\",\"updated_at\":\"${time}\",\"ori_id\":19115123,\"ori_order\":\"{\\\"title\\\":\\\"测试商品\\\",\\\"pic_url\\\":\\\"https://img.alicdn.com/i4/2201122445838/O1CN01TfLVOh1szqp2pHXtF_!!2201122445838-0-koubei.jpg\\\",\\\"shop_name\\\":\\\"${shop_name}\\\",\\\"pay_amount\\\":\\\"${price}\\\",\\\"settle_amount\\\":\\\"${price}\\\",\\\"trace_time\\\":\\\"${time}\\\",\\\"tk_create_time\\\":\\\"${time}\\\",\\\"pay_time\\\":\\\"${time}\\\",\\\"receive_time\\\":\\\"${time}\\\",\\\"settle_time\\\":\\\"${time}\\\",\\\"income\\\":\\\"2.93\\\",\\\"settle\\\":\\\"2.93\\\",\\\"item_id\\\":\\\"EA833A473DA4C3DC9E59570AEC49D368\\\",\\\"product_num\\\":1,\\\"unit_price\\\":\\\"${price}\\\",\\\"category_name\\\":\\\"馄饨抄手\\\",\\\"biz_order_id\\\":${order_no},\\\"parent_order_id\\\":${order_no},\\\"main_item_id\\\":\\\"\\\",\\\"main_item_title\\\":\\\"\\\",\\\"order_state\\\":${order_state},\\\"order_item_status_name\\\":\\\"${name}\\\",\\\"settle_state\\\":1,\\\"full_settle_amount\\\":\\\"${price}\\\",\\\"commission_rate\\\":\\\"0.06\\\",\\\"commission_fee\\\":\\\"1.43\\\",\\\"subsidy_rate\\\":\\\"0.0\\\",\\\"subsidy_fee\\\":\\\"0.0\\\",\\\"income_rate\\\":\\\"0.06\\\",\\\"stratify_rate\\\":\\\"\\\",\\\"deduct_rate\\\":\\\"\\\",\\\"platform_commission_rate\\\":\\\"0.1\\\",\\\"platform_commission_fee\\\":\\\"0.14\\\",\\\"channel_rate\\\":\\\"0.0\\\",\\\"channel_fee\\\":\\\"0.0\\\",\\\"media_id\\\":\\\"110001\\\",\\\"media_name\\\":\\\"必应鸟联盟\\\",\\\"ad_zone_id\\\":\\\"3982366\\\",\\\"ad_zone_name\\\":\\\"口令-神犬外卖\\\",\\\"activity_fee\\\":\\\"1.5\\\",\\\"activity_service_fee\\\":\\\"0.3\\\",\\\"activity_service_rate\\\":\\\"0.2\\\",\\\"gmt_modified\\\":\\\"${time}\\\",\\\"tag\\\":\\\"\\\",\\\"sid\\\":\\\"search_word_494\\\",\\\"platform_type\\\":2,\\\"activity_id\\\":672014,\\\"used_store_id\\\":\\\"\\\",\\\"pid\\\":\\\"alsc_12555424_110001_3982366\\\",\\\"relation_order_id\\\":0,\\\"flow_type\\\":3,\\\"order_item_status\\\":${order_state},\\\"activity_info_remark_list\\\":\\\"[]\\\",\\\"channel_right_id\\\":\\\"\\\",\\\"ext_info\\\":\\\"{\\\\\\\"attrOrderDesc\\\\\\\":\\\\\\\"否\\\\\\\",\\\\\\\"bwcActivityType\\\\\\\":\\\\\\\"reduce\\\\\\\",\\\\\\\"cityName\\\\\\\":\\\\\\\"上海\\\\\\\",\\\\\\\"alscOrderId\\\\\\\":\\\\\\\"${order_no}\\\\\\\",\\\\\\\"tpOrderId\\\\\\\":\\\\\\\"${order_no}\\\\\\\",\\\\\\\"isAllRefund\\\\\\\":\\\\\\\"null\\\\\\\",\\\\\\\"isSelfPurchase\\\\\\\":\\\\\\\"false\\\\\\\"}\\\"}\",\"client_id\":2,\"sid\":\"${sid}\",\"supplier_id\":104,\"order_type\":1401,\"sub_order_type\":\"饿了么外卖（活动订单）\",\"order_status\":3,\"parent_order_id\":\"${order_no}\",\"sub_order_id\":\"${order_no}\",\"item_id\":\"EA833A473DA4C3DC9E59570AEC49D368\",\"item_title\":\"蛋黄烧麦-福利\",\"item_cover\":\"https://img.alicdn.com/i4/2201122445838/O1CN01TfLVOh1szqp2pHXtF_!!2201122445838-0-koubei.jpg\",\"item_price\":${price},\"item_num\":1,\"order_price\":${price},\"pay_price\":${price},\"rate\":0.06,\"pre_commission\":1.43,\"commission\":1.43,\"third_service_fee\":0.14,\"third_service_ratio\":0.1,\"activity_fee\":1.5,\"activity_service_fee\":0.3,\"activity_service_ratio\":0.2,\"create_time\":\"${time}\",\"pay_time\":\"${time}\",\"receive_time\":\"${time}\",\"union_id\":\"12555424\",\"pid\":\"alsc_12555424_110001_3982366\",\"relation_id\":\"\"}",
    "ext":""
}
TEST_MYSQL = {
        'host': 'rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com',
        'port': 3306,
        'user': 'taomama',
        'passwd': '!qazxsw2',
        'db': '',
        'charset': 'utf8'
    }