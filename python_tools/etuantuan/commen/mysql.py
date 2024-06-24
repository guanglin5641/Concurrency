import pypymysql


class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host="rm-bp1xqhp60et1lx5z92o.mysql.rds.aliyuncs.com",
            user="taomama",
            password="!qazxsw2",
            db="etuantuan",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.conn.cursor()

    def select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def delete(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def update(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    db = DB()
    sql = """select bs.store_name ,bsp.longitude,bsp.latitude  from etuantuan.bwc_store_promotion bsp join etuantuan.bwc_store bs on bs.id = bsp.store_id  where promotion_end_date >= CURDATE() and promotion_status = 2;"""
    print(db.select(sql))