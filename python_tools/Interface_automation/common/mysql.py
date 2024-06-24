import pymysql
from dbutils.pooled_db import PooledDB
from pymysql import cursors
from interface_automation.common.config import conf


import time


class Pool(object):
    __pool = None
    __MAX_CONNECTIONS = 100  # 创建连接池的最大数量
    __MIN_CACHED = 10  # 连接池中空闲连接的初始数量
    __MAX_CACHED = 20  # 连接池中空闲连接的最大数量
    __MAX_SHARED = 0  # 池中共享连接的最大数量 默认为0，即每个连接都是专用的，不可共享(不常用，建议默认)
    __BLOCK = True  # 超过最大连接数量时候的表现，为True等待连接数量下降，为false直接报错处理
    __MAX_USAGE = 0  # 单个连接的最大重复使用次数，默认是0
    __RESET = True  # 当连接返回到池中时，重置连接的方式。默认True，总是执行回滚
    __SET_SESSION = ["SET AUTOCOMMIT = 1"]  # 设置自动提交

    def __init__(self, host, port, user, password, database):
        if not self.__pool:
            self.__class__.__pool = PooledDB(
                creator=pymysql,
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                maxconnections=self.__MAX_CONNECTIONS,
                mincached=self.__MIN_CACHED,
                maxcached=self.__MAX_CACHED,
                maxshared=self.__MAX_SHARED,
                blocking=self.__BLOCK,
                maxusage=self.__MAX_USAGE,
                setsession=self.__SET_SESSION,
                reset=self.__RESET,
                charset="utf8mb4",
            )

    def get_connect(self):
        return self.__pool.connection()


pool = connects_pool = Pool(
    host=conf.get_by_name("mysql.host"),
    port=conf.get_by_name("mysql.port"),
    user=conf.get_by_name("mysql.user"),
    password=conf.get_by_name("mysql.password"),
    database=conf.get_by_name("mysql.database"),
)


class DB(object):
    def __enter__(self):
        connect = pool.get_connect()
        cursor = connect.cursor(cursors.DictCursor)
        # https://blog.51cto.com/abyss/1736844
        # connect.autocommit = False # 如果使用连接池 则不能在取出后设置 而应该在创建线程池时设置
        self._connect = connect
        self._cursor = cursor
        return cursor

    """
    这三个值用于描述在上下文块中发生的异常：
        exc_type：表示异常的类型，通常是异常类的引用，例如 ValueError 或 TypeError。
        exc_value：表示引发的异常实例，通常包含异常的详细信息，例如异常消息。
        traceback：表示异常的回溯（traceback）对象，包含了关于异常的详细堆栈信息，可以用于调试。
    """

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self._connect.rollback()
        else:
            self._connect.commit()
        self._cursor.close()
        self._connect.close()

    @property
    def cursor(self):
        return self._cursor


if __name__ == "__main__":
    with DB() as db:
        aaa = 17065959539312966579
        for i in range(0, 1000):
            aaa += 1
            db.execute(f"INSERT INTO shenquan_dev.review_bwc_lock (updated_at,created_at,lock_no,client_user_id,lock_id,lock_time,unlock_time,lock_status,lock_sub_status,reason,version,reward_cent,real_reward_cent,reward_threshold_cent,real_reward_threshold_cent,shop_id,shop_name,shop_logo,activity_id,close_time,phone,order_no,finish_time,transfer_status,transfer_type,proves,transfer_time,admin_id,link_wx_appid,link_wx_path,sid)VALUES ('2024-01-30 14:26:33','2024-01-30 14:25:54',{aaa},245024690,350322271,1706595954243,1706597754243,3,0,'已完成',20240130,1000,800,1300,1300,'9B377B9AF4E8B0F7F2372A6781EC94E3','三米粥铺（仓前店）','https://img.alicdn.com//imgextra/i2/2206662726091/O1CN01w2otNy1urjMN6Q48O_!!2206662726091-0-koubei.jpg','2932001',0,'17111111113','804697104652300098',1706595992744,1,0,'',1706595992826,0,'wxece3a9a4c82f58c9','commercialize/pages/route-middle-page/index?scene=f32e7dafe4d246aea09acc6e0340b1ee','fb3f4434f6e0baff5ce395d907846b1d');")
            res = db.fetchone()
            print(res)
    # db = DB()
    # a = db.cursor()