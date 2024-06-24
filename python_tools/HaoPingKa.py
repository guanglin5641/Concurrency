import os
import pandas as pd
import pypymysql
from datetime import datetime


def mysql(city_list, start_time, end_time):
    # 连接数据库
    mysql = pymysql.connect(host='rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com', user='taomama', password='!qazxsw2',
                            db='shenquan', charset='utf8')
    # 创建游标
    cursor = mysql.cursor()
    # 构建SQL语句
    if len(city_list) == 1:
        city_condition = f"ccs.city = '{city_list[0]}'"
    else:
        city_condition = f"ccs.city IN {tuple(city_list)}"

    sql = f"SELECT ccr.id AS '好评id', ccs.name AS '店名', ccs.city AS '城市', wr.nickname AS '客服名称', cu.name AS '用户名称', ccr.image AS '图片', ccr.reward AS '返现金额', ccr.created_at AS '创建时间', ccr.updated_at AS '更新时间' FROM shenquan.comment_cashback_record ccr JOIN shenquan.comment_cashback_shop ccs JOIN client_user cu JOIN wechat_robot.wechat_robot wr ON ccr.shop_id = ccs.id AND cu.client_user_id = ccr.client_user_id AND cu.wework_id = wr.wxid WHERE {city_condition} AND ccr.created_at BETWEEN '{start_time}' AND '{end_time}';"
    # 随机数
    now = datetime.now()
    formatted_time = str(now.strftime("%Y%m%d%H%M%S"))
    print(formatted_time)

    # 执行SQL语句
    cursor.execute(sql)
    # 获取数据
    data = cursor.fetchall()
    # 将数据转换为DataFrame
    df = pd.DataFrame(data, columns=['好评id', '店名', '城市', '客服名称', '用户名称', '图片', '返现金额', '创建时间', '更新时间'])
    # 获取桌面路径
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    # 保存为Excel文件
    file_path = os.path.join(desktop_path, formatted_time+city_list[0] + '上传.xlsx')
    df.to_excel(file_path, index=False)
    # 关闭数据库连接
    mysql.close()
    return ("提示", "数据已保存为Excel文件")
