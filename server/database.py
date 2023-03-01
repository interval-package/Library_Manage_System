import sqlite3
import json
import pandas as pd

# sql = sqlite3.connect("./info.db")

sql = sqlite3.connect(".\data\library_info_core.db")


def get_tab(tar):
    return pd.read_sql_query(tar, con=sql).tostring


def add_user(id, pwd):
    sql.execute(f"insert into User(UserId, Role, Password)values('{str(id)}', 2,'{str(pwd)}')")


def check_user(id, pwd) -> bool:
    res = sql.execute(f"SELECT EXISTS(SELECT 1 FROM User WHERE UserId = '{id}' and Password = '{pwd}') as has_user")
    return res.fetchall()[0][0] == 1


if __name__ == '__main__':
    print(check_user("zza", '0'))
    pass
