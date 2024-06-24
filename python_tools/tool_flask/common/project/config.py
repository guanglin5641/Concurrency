from peewee import MySQLDatabase

DATABASE = 'date'
USER = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = 3306

db = MySQLDatabase(DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
