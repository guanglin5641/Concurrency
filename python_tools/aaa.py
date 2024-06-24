import pymysql
import datetime


def user_db(sql) :
    db = pymysql.connect(
        host="rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com" ,
        user="taomama" ,
        password="!qazxsw2" ,
        database="shenquan" ,
        port=3306
        )
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    return res


if __name__ == '__main__' :
    user_count = '''select id from shenquan_dev.open_user ou limit 10;'''
    counts = user_db(user_count)
    countes = [i[0] for i in counts]
    print(countes)

    for f in countes :
        select_user_sql = f'''select id, create_time, union_id, source_channel_type, source_add_time, source_channel_uid, qrcode_id 
                              from shenquan_dev.open_user ou where id = {f};'''
        select_user_db = user_db(select_user_sql)

        if not select_user_db :
            continue

        open_user_id = select_user_db[0][0]
        open_user_time = int(select_user_db[0][1])
        open_user_union_id = select_user_db[0][2]
        open_user_source_channel_type = select_user_db[0][3]
        open_user_source_add_time = int(select_user_db[0][4])
        open_user_source_channel_uid = str(select_user_db[0][5])
        open_user_qrcode_id = select_user_db[0][6]

        thirld_sql = f'''SELECT 
                            MIN(gzh_first_subscribe_time) AS gzh_first_subscribe_time,
                            qrcode_id,
                            app_id
                        FROM 
                            shenquan_dev.open_third_party_login 
                        WHERE 
                            open_user_id = {open_user_id} 
                            AND gzh_first_subscribe_time IS NOT NULL;'''
        thirld_db = user_db(thirld_sql)

        if not thirld_db :
            # 如果 third_db 为空，则直接处理
            if open_user_time == 0 :
                open_user_time = float('inf')
            if open_user_source_add_time == 0 :
                open_user_source_add_time = float('inf')

            if open_user_time <= open_user_source_add_time :
                reality_source_channel_type = 1
                reality_source_add_time = open_user_time
            else :
                reality_source_channel_type = 2
                reality_source_add_time = open_user_source_add_time
        else :
            gzh_first_subscribe_time = int(thirld_db[0][0])
            qrcode_id = thirld_db[0][1]
            app_id = thirld_db[0][2]

            wechart_sql = f'''select follow_user_id, follow_time, channel_code_id 
                              from wechat_robot.work_wx_external_contact wwec 
                              where unionid = '{open_user_union_id}' and wechat_service_id = 1;'''
            wechart_db = user_db(wechart_sql)

            if not wechart_db :
                continue

            follow_user_id = wechart_db[0][0]
            follow_time = wechart_db[0][1]
            follow_time_sm = int(follow_time.timestamp())
            channel_code_id = wechart_db[0][2]

            if follow_time_sm == 0 :
                follow_time_sm = float('inf')

            if open_user_time == 0 :
                open_user_time = float('inf')

            if gzh_first_subscribe_time == 0 :
                gzh_first_subscribe_time = float('inf')

            if open_user_time <= follow_time_sm :
                reality_source_channel_type = 1
                reality_source_add_time = open_user_time
                reality_source_channel_uid = 2
            else :
                reality_source_channel_type = 3
                reality_source_add_time = follow_time_sm
                reality_source_channel_uid = follow_user_id
                reality_qcode_id = channel_code_id

        print("Results:" , open_user_id , reality_source_channel_type , reality_source_add_time )
