import os
class Config:
    KEY = os.getenv('KEY', 'bdapba')
    SECRET = os.getenv('SECRET', 'c2b7efd73fbad150a4d51c5b6bf71172')
    HOST = os.getenv('HOST', 'test.warehouse.biyingniao.com')
    TOKEN = os.getenv('TOKEN', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...')
    URL = os.getenv('URL', '/api/cps/bwc_shops')
    SHOP_LIST_JSON = {
        ...
    }
