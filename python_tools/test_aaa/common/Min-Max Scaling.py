from test_aaa.common.mysql import DB
import time
def select_shop_list(X):
    db = DB()
    sql = '''
        select 
        create_time 
        from 
        bwc_dev.bwc_store_promotion bsp 
        where 
        promotion_status = 2 
        and 
        promotion_start_date <= '2023-11-15' 
        and 
        promotion_end_date >= '2023-11-15' 
        and 
        mall_user_id != 69
    '''
    create_time = db.cursor(sql)
    mun = len(create_time)
    # print(mun)
    create_time_list = []
    for i in range(mun):
        create_time_list.append(create_time[i]["create_time"])
    print(create_time_list)
    min_value = min(create_time_list)
    current_timestamp = time.time()
    X_normalized = (X-min_value)/(current_timestamp-min_value)
    return (X_normalized)

if __name__ == "__main__":
    print(select_shop_list())

