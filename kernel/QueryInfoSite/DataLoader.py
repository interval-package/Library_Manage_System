# import ... other sql libs
import os
import sqlite3 as sql

# 这里要做的就是把数据访问的工作给隐藏起来
data_path = os.path.join(os.getcwd(), 'data', 'library_info_core.db')


def quote(string):
    return "'{}'".format(string)


class DataBaseAct(object):
    # ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

    data_path = os.path.join(os.getcwd(), '../../data', 'library_info_core.db')

    def __init__(self, action: str):
        self.data_path = os.path.join(os.getcwd(), '../../data', 'database', 'library_info_core.db')
        pass


class DataLoader(object):
    data_path = os.path.join(os.getcwd(), '../../data', 'library_info_core.db')


class LoginUserDataLoader(DataLoader):
    def __init__(self, user, password):
        with sql.connect(DataBaseAct.data_path) as conn:
            try:
                cursor = conn.execute("""
                    select * from User
                    where UserId = %s
                    and UserName = %s
                    """ % (quote(user), quote(password)))
                # 这个地方要注意，如果对于自字符串进行比较的话，要有''
            except sql.DatabaseError as e:
                print(repr(e))
            res = cursor.fetchall()[0]


# 对数据管理进行了尝试，对于数据模型的设计还是用sql语言来进行实现，我们这里只要进行访问就行了


if __name__ == '__main__':
    data_path = os.path.join(os.getcwd(), '../../data', 'library_info_core.db')
    print(data_path)

    # sqlCommand = 'insert into book (BookId, BookName) values(?, ?)'
    # datas = [
    #     (23, 'book1'),
    #     (123, 'book2'),
    # ]

    with sql.connect(DataBaseAct.data_path) as conn:
        try:
            cursor = conn.execute("""
                select * from User
                where User.UserId = %s
                """ % ("'0000'"))
            # 这个地方要注意，如果对于自字符串进行比较的话，要有''
            # cursor = conn.execute("""
            #     select * from User
            #     where UserName = 'zza'
            #     """)
        except sql.DatabaseError as e:
            print(repr(e))

        # print('000000' in cursor)
        res = cursor.fetchall()
        print(res)
        for row in cursor:
            print(row)
            for i in row:
                print(type(i))

    # # conn = sqlite3.connect(data_path)
    # with sql.connect(data_path) as conn:
    #     try:
    #         conn.executemany(sqlCommand, datas)
    #     except Exception as e:
    #         warnings.warn(repr(e))
    #         pass
    #     cursor = conn.execute("select * from User")
    #     print(cursor)
    #     for row in cursor:
    #         for i in row:
    #             print(i)
