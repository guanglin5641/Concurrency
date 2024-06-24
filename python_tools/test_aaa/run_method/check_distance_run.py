import test_aaa.common.mysql
import test_aaa.connector.JuLi

def select_stort():
    db = test_aaa.common.mysql.DB()
    sql = '''
    select 
    bs.id ,
    bs.longitude ,
    bs.latitude ,
    bs.address_detail  
    from 
    etuantuan.bwc_store_promotion bsp 
    join 
    etuantuan.bwc_store bs 
    on 
    bs.id =bsp.store_id 
    where 
    promotion_start_date <= CURDATE() 
    and 
    promotion_end_date >= CURDATE() 
    and 
    promotion_status = 2
    group by bs.id ;
    '''

    data_list = db.select(sql)
    x = len(data_list)
    for i in range(x):
        id = data_list[i]["id"]
        longitude = data_list[i]["longitude"]
        latitude = data_list[i]["latitude"]
        address_detail = data_list[i]["address_detail"].replace('#', '')
        (juli_longitude,juli_latitude,juli_address_detail)=test_aaa.connector.JuLi.baidu_dis(address_detail)
        coord1= (latitude,longitude)
        coord2 = (juli_latitude,juli_longitude)
        distance_difference=test_aaa.connector.JuLi.calculate_distance(coord1,coord2)
        if distance_difference>5000:
            print(id,juli_longitude,juli_longitude,distance_difference)
        else:
            pass
    return data_list
if __name__ == '__main__':
    select_stort()
