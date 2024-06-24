
import redis

redis_conn = redis.Redis(
    host='127.0.0.1:',
    port=6379,
    password='123456',
    db=0,
    decode_responses=True)

print(redis_conn)
# Redis<ConnectionPool<Connection<host=192.168.xxx.xxx,port=16379,db=0>>>

redis_conn.set('name', 'xiaoming')