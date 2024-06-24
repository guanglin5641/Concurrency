from datetime import datetime
from common.constant import BYN_SETING
from common.myslq import MysqlHelper
class now_time_brand():
    #init
    def __init__(self,):
        self.brand_sql = MysqlHelper(BYN_SETING)
        self.data_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pass
    # 查询品牌显示什么
    def search_brand(self) :
        # 查询活动关联的品牌
        act_sql = f'''
            select 
                sb.id,
                sb.brand_name ,
                a.title 
                from
                shenquan_dev.activity a 
                join shenquan_dev.shop_brands sb on a.self_brand_id = sb.id 
                where sb.status =1;
            '''
        data = self.brand_sql.get_all(act_sql)
        return data
    # 查询霸王餐店铺显示什么
    def search_zero(self) :
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        zero_sql = f'''
            select 
                sb.id ,
                sb.brand_name 
                from 
                shenquan_dev.shop_brands sb 
                join shenquan_dev.shop s on sb.id = s.brand_id 
                join shenquan_dev.elm_shop_act_rels esar on s.ad_store_id COLLATE utf8mb4_unicode_ci = esar.shop_code COLLATE utf8mb4_unicode_ci
                where 
                sb.status =1 
                and esar.promotion_state =2 
                and %s between esar.start_date and esar.end_date 
                and esar.terminate_time is null;
            '''
        data = self.brand_sql.get_all(zero_sql, self.data_now)
        return data



