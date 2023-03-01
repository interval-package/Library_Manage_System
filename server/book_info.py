from server.database import *
from kernel.QueryInfoSite.QueryInfo import *

book_cols = ["book_id", "book_name"]


def check_login(user_id, user_pwd):
    res = dict()
    cur = sql.execute(f"select * from user_info where user_id = '{user_id}' and user_pwd = '{user_pwd}'")
    u_info = cur.fetchall()
    return u_info


def fetch_info(book_id):
    res = dict()

    cur = sql.execute(f"select * from book_info where book_id = '{book_id}'")
    column_list = [column[0] for column in cur.description]
    cur = cur.fetchall()
    if cur:
        for detail in zip(column_list, cur[0]):
            res[detail[0]] = detail[1]
        pass
    else:
        for detail in book_cols:
            res[detail] = "not find"
        pass

    return res


def rent_book(user_id, user_pwd, book_id):
    res = dict()
    if check_login(user_id, user_pwd):
        try:
            Add_RentHis(user_id, book_id)
            res["ans"] = "success"
        except RentRefuse as e:
            res["ans"] = "not allow"
        except Exception as e:
            res["ans"] = "error"
    else:
        res["ans"] = "fail"
    return res
