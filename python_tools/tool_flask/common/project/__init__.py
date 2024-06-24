# __init__.py

from config import db
from models import ZeroProduct

def create_tables():
    # 先检查表是否存在，如果不存在则创建
    if not ZeroProduct.table_exists():
        with db:
            db.create_tables([ZeroProduct])

# 在模块导入时执行创建表的逻辑
create_tables()

