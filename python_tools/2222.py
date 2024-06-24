import pymysql
import datetime
import time
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

thirld = 1704857407
h5 = 1709189778

if __name__ == '__main__' :
    user_count = '''select id from shenquan.open_user ou where union_id != '' order by id desc limit 500, 1000;'''
    counts = user_db(user_count)
    countes = [i[0] for i in counts]
    print(len(countes))
    print(countes)


    for f in countes :
        select_user_sql = f'''select id, create_time, union_id, source_channel_type, source_add_time, source_channel_uid, qrcode_id 
                              from shenquan.open_user ou where id = {f};'''
        # 打印数据
        select_user_db = user_db(select_user_sql)

        if not select_user_db :
            # print("没用户"）
            pass
        else:
            # 用户ID
            open_user_id = select_user_db[0][0]
            # print(open_user_id)
            # 用户创建时间
            open_user_time = int(select_user_db[0][1])
            # print(open_user_time)
            # 用户编码
            open_user_union_id = select_user_db[0][2]
            # print(open_user_union_id)
            # 用户渠道
            open_user_source_channel_type = select_user_db[0][3]
            # print(open_user_source_channel_type)
            # 用户渠道时间
            open_user_source_add_time = int(select_user_db[0][4])
            # print(open_user_source_add_time)
            # 用户渠道UID
            open_user_source_channel_uid = str(select_user_db[0][5])
            # print(open_user_source_channel_uid)
            # 用户渠道编码
            open_user_qrcode_id = select_user_db[0][6]
            # print(open_user_qrcode_id)

            # thirld表格数据
        thirld_sql = f'''SELECT 
                            MIN(gzh_first_subscribe_time) AS gzh_first_subscribe_time,
                            MIN(create_time) AS create_time,
                            qrcode_id,
                            app_id,
                            id
                        FROM 
                            shenquan.open_third_party_login 
                        WHERE 
                            open_user_id = {open_user_id} 
                            AND gzh_first_subscribe_time IS NOT NULL; '''
        thirld_db = user_db(thirld_sql)

        if thirld_db[0][4] is None:
            # print("没三方用户")
            gzh_first_subscribe_time = 0
            # print(gzh_first_subscribe_time)
            thirld_create_time = 0
            # 公众号编码
            qrcode_id = 0
            # print(qrcode_id)
            # 公众号标识
            app_id = 0
            # print(app_id)
        else:
            # print(thirld_db)
            # 公众号加入时间
            gzh_first_subscribe_time = int(thirld_db[0][0])
            # print(gzh_first_subscribe_time)
            thirld_create_time = int(thirld_db[0][1])
            # 公众号编码
            qrcode_id = thirld_db[0][2]
            # print(qrcode_id)
            # 公众号标识
            app_id = thirld_db[0][3]
            # print(app_id)

            # wechart表格数据
        wechart_sql = f'''select follow_user_id, follow_time, channel_code_id ,id
                          from wechat_robot.work_wx_external_contact wwec 
                          where unionid = '{open_user_union_id}' and wechat_service_id = 1;'''
        wechart_db = user_db(wechart_sql)
        if not wechart_db :
            # print("没企微用户")
            follow_user_id = 0
            # print(follow_user_id)
            # 加个号时间
            follow_time = 0
            # 将follow_time转成秒单位时间戳
            follow_time_sm = 0
            # print(follow_time_sm)
            # 个号编码
            channel_code_id = 0
        else:
            # 个号人
            follow_user_id = wechart_db[0][0]
            # print(follow_user_id)
            # 加个号时间
            follow_time = wechart_db[0][1]
            # 将follow_time转成秒单位时间戳
            follow_time_sm = int(follow_time.timestamp())
            # print(follow_time_sm)
            # 个号编码
            channel_code_id = wechart_db[0][2]
            # print("code",channel_code_id)
        MAX_TIME = float('inf')
        thirld_create_time = MAX_TIME if thirld_create_time == 0 else int(thirld_create_time)
        follow_time_sm = MAX_TIME if follow_time_sm == 0 else int(follow_time_sm)
        gzh_first_subscribe_time = MAX_TIME if gzh_first_subscribe_time == 0 else int(gzh_first_subscribe_time)
        if not wechart_db:
            if thirld_db[0][4] is None:
                reality_open_user_id = open_user_id
                reality_source_channel_type = 1
                reality_source_add_time = thirld_create_time
                reality_source_channel_uid = 2
                if reality_source_channel_type == open_user_source_channel_type and reality_source_add_time == open_user_source_add_time and reality_source_channel_uid == open_user_source_channel_uid:
                    print("true",open_user_id)
                else:
                    print("bb",reality_open_user_id, reality_source_channel_type, reality_source_add_time, reality_source_channel_uid,
                          reality_open_user_id,open_user_source_channel_type,open_user_source_add_time,open_user_source_channel_uid)
            else:
                if thirld_create_time < gzh_first_subscribe_time:
                    reality_open_user_id = open_user_id
                    reality_source_channel_type = 1
                    reality_source_add_time = thirld_create_time
                    reality_source_channel_uid = 2
                    if int(reality_source_channel_type) == int(open_user_source_channel_type) and int(reality_source_add_time) == int(open_user_source_add_time) and int(reality_source_channel_uid) == int(open_user_source_channel_uid) :
                        print("true",open_user_id)
                    else:
                        print("aaa",reality_open_user_id , reality_source_channel_type , reality_source_add_time ,
                              reality_source_channel_uid ,
                              reality_open_user_id , open_user_source_channel_type , open_user_source_add_time ,
                              open_user_source_channel_uid)
                elif thirld_create_time >= gzh_first_subscribe_time:
                    reality_open_user_id = open_user_id
                    reality_source_channel_type = 2
                    reality_source_add_time = gzh_first_subscribe_time
                    reality_source_channel_uid = app_id
                    reality_qcode_id = qrcode_id
                    if reality_source_channel_type == open_user_source_channel_type \
                            and int(reality_source_add_time) == int(open_user_source_add_time) \
                            and int(reality_source_channel_uid) == int(open_user_source_channel_uid) \
                            and reality_qcode_id == open_user_qrcode_id:
                        print("true",open_user_id)
                    else:
                        print("cccc",reality_open_user_id , reality_source_channel_type , reality_source_add_time ,
                              reality_source_channel_uid ,reality_qcode_id,
                              reality_open_user_id , open_user_source_channel_type , open_user_source_add_time ,
                              open_user_source_channel_uid,open_user_qrcode_id)
                else:
                    print("错误")
        elif thirld_db[0][4] is None:
            # if thirld_create_time > follow_time_sm:
            #     reality_open_user_id = open_user_id
            #     reality_source_channel_type = 1
            #     reality_source_add_time = thirld_create_time
            #     reality_source_channel_uid = 2
            #     if reality_source_channel_type == open_user_source_channel_type and reality_source_add_time == open_user_source_add_time and reality_source_channel_uid == open_user_source_channel_uid :
            #         print("true",open_user_id)
            #     else:
            #         print(reality_open_user_id , reality_source_channel_type , reality_source_add_time ,
            #               reality_source_channel_uid ,
            #               reality_open_user_id , open_user_source_channel_type , open_user_source_add_time ,
            #               open_user_source_channel_uid)
            # elif thirld_create_time <= follow_time_sm:
            #     reality_open_user_id = open_user_id
            #     reality_source_channel_type = 3
            #     reality_source_add_time = follow_time_sm
            #     reality_source_channel_uid = follow_user_id
            #     reality_qcode_id = channel_code_id
            #     if reality_source_channel_type == open_user_source_channel_type and reality_source_add_time == open_user_source_add_time and reality_source_channel_uid == open_user_source_channel_uid and reality_qcode_id == open_user_qrcode_id :
            #         print("true",open_user_id)
            #     else:
            #         print(reality_open_user_id , reality_source_channel_type , reality_source_add_time ,
            #               reality_source_channel_uid ,
            #               reality_open_user_id , open_user_source_channel_type , open_user_source_add_time ,
            #               open_user_source_channel_uid)
            reality_open_user_id = open_user_id
            reality_source_channel_type = 3
            reality_source_add_time = int(follow_time_sm)
            reality_source_channel_uid = int(follow_user_id)
            if reality_source_channel_type == open_user_source_channel_type and reality_source_add_time == open_user_source_add_time and reality_source_channel_uid == int(open_user_source_channel_uid) :
                print("true",open_user_id)
            else:
                print(reality_open_user_id , reality_source_channel_type , reality_source_add_time ,
                      reality_source_channel_uid ,
                      reality_open_user_id , open_user_source_channel_type , open_user_source_add_time ,
                      open_user_source_channel_uid)

        else:
            reality_open_user_id = open_user_id
            reality_source_add_time = min(thirld_create_time,follow_time_sm,gzh_first_subscribe_time)
            reality_source_channel_type = (thirld_create_time,gzh_first_subscribe_time, follow_time_sm).index(reality_source_add_time) + 1
            reality_source_channel_uid = (2, app_id, follow_user_id)[reality_source_channel_type - 1]
            # reality_qcode_id = (0, app_id,channel_code_id)[reality_source_channel_type - 1]
            if int(reality_source_channel_type) == int(open_user_source_channel_type) and int(reality_source_add_time) == int(open_user_source_add_time) :#and reality_source_channel_uid == open_user_source_channel_uid and reality_qcode_id == open_user_qrcode_id:
                print("true",open_user_id)
            else:
                print("aaa",reality_open_user_id , reality_source_channel_type , reality_source_add_time ,
                      reality_source_channel_uid ,
                      reality_open_user_id , open_user_source_channel_type , open_user_source_add_time ,
                      open_user_source_channel_uid)
                continue