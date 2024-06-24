import pymysql
def lianjie_sql(sql):
    connet = pymysql.connect(host='rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com',user='taomama',password='!qazxsw2',db='shenquan_dev')
    cursor = connet.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connet.close()
    return data
#订单推广服务费

def tg (a,order_no):
    if a == 1 :
        aa = 'out_activity_fee - out_activity_service_fee'
    elif a == 2:
        aa = 'out_commission_fee - out_platform_commission_fee'
    else:
        return
    sql = f'''
    select 
    {aa}
    from 
    shenquan_dev.collect_order co where order_no = '{order_no}' order by id desc;
    '''
    data = lianjie_sql(sql)
    return data[0][0]
if __name__ == '__main__':
    #1是服务费
    #2是佣金
    print(tg(1,"804697104652300095"))