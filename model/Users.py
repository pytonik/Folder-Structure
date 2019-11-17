from pytonik import Web

def insert_users(data):
    db = Web.Model().db
    query_register = "INSERT INTO usertable (firstnamamvc, lastnamemvc, usernamemvc, passwordmvc, createddatemvc) " \
                     "VALUES " \
                     "(%(firstnamamvc)s, %(lastnamemvc)s, %(usernamemvc)s, %(passwordmvc)s, %(createddatemvc)s)"
    db.query(query_register, data)
    return db.save()


def check_user_count(useremail):
    db = Web.Model().db
    query_check = "SELECT * FROM usertable WHERE usernamemvc = '{usernamemvc}'".format(usernamemvc=useremail)
    db.query(query_check)
    return db.countall()
