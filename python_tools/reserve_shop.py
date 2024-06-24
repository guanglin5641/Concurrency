import pymysql

def shop_db(sql_list):
   db = pymysql.connect(host="rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com", user="taomama", password="!qazxsw2", database="shenquan", port=3306)
   cursor = db.cursor()
   sql = sql_list
   cursor.execute(sql)
   res = cursor.fetchall()
   return res

sql= "select count(*) a,ori_shop_name,max(bonus_fee)  from elm_shop_act_rels esar where promotion_state = 2  and end_date > DATE_FORMAT(NOW(), '%Y-%m-%d %H:%i:%s') and terminate_time is null group by ori_shop_name ,shop_code having a>1 order by  a desc ;"