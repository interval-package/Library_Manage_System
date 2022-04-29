QueryMethod = 'sqlite'
# QueryMethod = 'sql_server'

if QueryMethod == 'sqlite':
    from kernel.QueryInfoSite.QueryInfo_sqlite import *
elif QueryMethod == 'sql_server':
    from kernel.QueryInfoSite.QueryInfo_MsSql import *


def Query_UserRentingHis(user_id):
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
                    select Book.BookId, Book.BookName, BookType.TypeName, RentHistory.RentDay, RentHistory.ReturnDate
                    from User, Book, RentHistory, BookType
                    where User.UserId = %s and BookType.TypeId = Book.TypeId
                    and User.UserId = RentHistory.UserId and Book.BookId = RentHistory.BookId
                """ % (quote(user_id)))
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_BookRank():
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
                select Book.BookId, BookName, times, Stock, Price, TypeName from Book, BookType,
                (
                select BookId, count(*) as times from RentHistory
                group by BookId
                ) as temp
                where Book.BookId = temp.BookId and Book.TypeId = BookType.TypeId
                order by times desc""")
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_UserRank():
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
                select UserName, User.UserId, times from User, 
                (
                select UserId, count(*) as times from RentHistory
                group by UserId
                )as temp
                where User.UserId = temp.UserId
                order by times desc""")
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_BookType():
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
                select * from BookType
                """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_BookType_Id():
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
                select TypeId
                from BookType
                """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_Book(TypeName, BookInfo):
    res = None
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
                select Book.BookName, Book.BookId
                from Book, BookType
                where Book.TypeId = BookType.TypeId and BookType.TypeName = {0}
                and Book.BookName like '%{1}%' and Book.Stock > 0
                """.format(quote(TypeName), BookInfo))
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_UnReturned_Book(UserId):
    res = None
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
                select User.UserId, User.UserName, RentHistory.BookId, Book.BookName, 
                RentHistory.RentDay
                from
                RentHistory, User, Book
                where 
                User.UserId = RentHistory.UserId
                and Book.BookId = RentHistory.BookId
                and RentHistory.ReturnDate is null 
                and User.UserId is '{}'
                """.format(str(UserId)))
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_Price_Remain(UserId, BookId=None, RentDate=None):
    req = """
        select * from UnreturnPrice
        where UserId = '{}'
        """.format(str(UserId))

    if BookId is not None:
        req += " and BookId = '{}'".format(str(BookId))

    if RentDate is not None:
        req += " and RentDay = '{}'".format(str(RentDate))

    res = None
    with connGetter() as conn:
        try:
            cursor = connAction(conn, req)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Modify_Return(tar):
    if len(tar) != 3:
        raise ReturnRefuse()
    UserId, BookId, RentDate = tar
    with connGetter() as conn:
        connAction(conn, """
        update RentHistory
        set ReturnDate = date('now')
        where UserId = '{}'
        and BookId = '{}'
        and RentDay = '{}'
        and ReturnDate is null
        """.format(str(UserId), str(BookId), RentDate))
    print("return success")
    pass


def RentCertification(UserId, BookId) -> bool:
    with connGetter() as conn:
        cursor = connAction(conn, """
            select * from UserUnReturn_Count
            where UserId = '{}'
        """.format(str(UserId)))
        tar = cursor.fetchall()
        if len(tar) == 0:
            pass
        else:
            if tar[0][1] >= tar[0][2]:
                raise RentRefuse("too many books")
    with connGetter() as conn:
        cursor = connAction(conn, """
            select * from BookRemain
            where BookId = '{}'
        """.format(str(BookId)))
        tar = cursor.fetchall()
        if len(tar) == 0:
            pass
        else:
            if tar[0][1] <= 0:
                raise RentRefuse("no book remain")
    return True


def Add_RentHis(UserId, BookId):
    RentCertification(UserId, BookId)
    with connGetter() as conn:
        connAction(conn, """
            insert into RentHistory
            values
            ({0},{1},date('now'),null)
            """.format(quote(UserId), quote(BookId)))
    pass


def Add_Book(BookId, BookName, stock, price, BookType):
    with connGetter() as conn:
        connAction(conn, """
        insert into Book(BookId,BookName,Stock,Price,TypeId)
        values(
        '{}', '{}', {}, {}, '{}'
        )
        """.format(str(BookId), str(BookName), stock, price, str(BookType)))
    pass


def Add_BookType(Id, Name):
    with connGetter() as conn:
        connAction(conn,
                   """
        insert into BookType
        values(
        '{}', '{}'
        )
        """.format(str(Id), str(Name)))
    pass


def Add_User(UserId, UserName, Role, Password):
    with connGetter() as conn:
        connAction(conn,
                   """
                insert into User
                values
                (%s,%s,%d,%s)
            """ % (quote(UserId), UserName, Role, quote(Password)))


def Update_UserInfo(pack):
    try:
        with connGetter() as conn:
            connAction(conn,
                       """
                update User set UserName = '{}',
                Password = '{}',
                Role = '{}'
                where UserId = '{}' 
                """.format(pack['name'], pack['password'], pack['role'], pack['id']))
    except Exception as e:
        raise RentRefuse(repr(e))
    pass


def Update_RentDate(UserId, BookId, RentDate):
    try:
        with connGetter() as conn:
            connAction(conn,
                       """
            update UnreturnPrice
            set RentDay = date('now')
            where UserId = '{}'
            and BookId = '{}'
            and RentDay = '{}'
            """.format(str(UserId), str(BookId), RentDate))
    except Exception as e:
        raise RentRefuse(repr(e))
    pass


def Update_BookInfo(pack):
    try:
        with connGetter() as conn:
            connAction(conn,
                       """
                update Book set BookName = '{}',
                Stock = '{}',
                Price = '{}',
                TypeId = '{}'
                where UserId = '{}' 
                """.format(pack['name'], pack['stock'], pack['price'], pack['type id'], pack['id']))
    except Exception as e:
        raise RentRefuse(repr(e))
    pass


def FetchAllBooks():
    res = None
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
            select * from Book
            """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def FetchAllBookType():
    res = None
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
            select * from BookType
            """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def FetchAllRoleTypes():
    res = None
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
            select * from UserRole
            """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def FetchAllUser():
    res = None
    with connGetter() as conn:
        try:
            cursor = connAction(conn, """
            select * from User
            """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


if __name__ == '__main__':
    pass
