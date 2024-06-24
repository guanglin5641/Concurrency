from pymysql import connect

class MysqlHelper:
    def __init__(self, conn_params):
        self.__host = conn_params.get('host')
        self.__port = conn_params.get('port', 3306)
        self.__db = conn_params.get('db')
        self.__user = conn_params.get('user')
        self.__passwd = conn_params.get('passwd')
        self.__charset = conn_params.get('charset', 'utf8')
        self.__conn = None
        self.__cursor = None

    def __connect(self):
        self.__conn = connect(
            host=self.__host,
            port=self.__port,
            db=self.__db,
            user=self.__user,
            passwd=self.__passwd,
            charset=self.__charset
        )
        self.__cursor = self.__conn.cursor()

    def __close(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__conn:
            self.__conn.close()

    def get_one(self, sql, params=None):
        result = None
        try:
            self.__connect()
            self.__cursor.execute(sql, params)
            result = self.__cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.__close()
        return result

    def get_all(self, sql, params=None):
        lst = ()
        try:
            self.__connect()
            self.__cursor.execute(sql, params)
            lst = self.__cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.__close()
        return lst

    def insert(self, sql, params=None):
        return self.__edit(sql, params)

    def update(self, sql, params=None):
        return self.__edit(sql, params)

    def delete(self, sql, params=None):
        return self.__edit(sql, params)

    def __edit(self, sql, params=None):
        count = 0
        try:
            self.__connect()
            count = self.__cursor.execute(sql, params)
            self.__conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.__close()
        return count

if __name__ == '__main__':
    conn_params = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': '',
        'db': 'date',
        'charset': 'utf8'
    }
    db_helper = MysqlHelper(conn_params)
    sql = 'SELECT * FROM zero_product'
    params = ()
    print(db_helper.get_one(sql, params))
