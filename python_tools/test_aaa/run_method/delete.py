import aaa.common.mysql
db = aaa.common.mysql.DB()
def delete():
    sql1= '''
    DELETE FROM shenquan_dev.client_user  WHERE open_user_id = (select open_user_id  from shenquan_dev.client_user cu where name = '范铭哲Rufus');
'''
    sql2 = '''
        DELETE FROM shenquan_dev.open_user  WHERE id = (select open_user_id  from shenquan_dev.client_user cu where name = '范铭哲Rufus');
    '''
    sql3 = '''
        DELETE FROM shenquan_dev.open_third_party_login  WHERE open_user_id = (select open_user_id  from shenquan_dev.client_user cu where name = '范铭哲Rufus');
    '''
    db.delete(sql1)
    db.delete(sql2)
    db.delete(sql3)
    return ()
if __name__ == "__main__":
    delete()
    db.close()