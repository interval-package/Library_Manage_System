from kernel.QueryInfoSite.DataLoader import sql, data_path, quote
from kernel.QueryInfoSite.ExceptionClasses_Query import *
import pandas as pd


def Query_UserRentingHis(user_id):
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                    select Book.BookId, Book.BookName, BookType.TypeName, RentHistory.RentDay, RentHistory.ReturnDate
                    from User, Book, RentHistory, BookType
                    where User.UserId = %s and BookType.TypeId = Book.Type
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select Book.BookId, BookName, times, Stock, Price, TypeName from Book, BookType,
                (
                select BookId, count(*) as times from RentHistory
                group by BookId
                ) as temp
                where Book.BookId = temp.BookId and Book.Type = BookType.TypeId
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select Book.BookName, Book.BookId
                from Book, BookType
                where Book.Type = BookType.TypeId and BookType.TypeName = {0}
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
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


def Modify_Return(tar):
    if len(tar) != 3:
        return
    UserId, BookId, RentDate = tar
    with sql.connect(data_path) as conn:
        conn.execute("""
        update RentHistory
        set ReturnDate = date('now')
        where UserId = '{}'
        and BookId = '{}'
        and RentDay = '{}'
        and ReturnDate is null
        """.format(str(UserId), str(BookId), RentDate))
    pass


def RentCertification(UserId) -> bool:
    with sql.connect(data_path) as conn:
        cursor = conn.execute("""
            select * from UserUnReturn_Count
            where UserId = '{}'
        """.format(str(UserId)))
        tar = cursor.fetchall()
    if len(tar) == 0:
        return True
    else:
        if tar[0][1] >= tar[0][2]:
            return False
    return True


def Add_RentHis(UserId, BookId):
    if RentCertification(UserId):
        with sql.connect(data_path) as conn:
            conn.execute("""
                insert into RentHistory
                values
                ({0},{1},date('now'),null)
                """.format(quote(UserId), quote(BookId)))
    else:
        raise RentRefuse()
    pass


def Add_Book(BookId, BookName, stock, price, BookType):
    with sql.connect(data_path) as conn:
        conn.execute("""
        insert into Book
        values(
        '{}', '{}', {}, {}, '{}'
        )
        """.format(str(BookId), str(BookName), stock, price, str(BookType)))
    pass


def Add_BookType(Id, Name):
    with sql.connect(data_path) as conn:
        conn.execute("""
        insert into BookType
        values(
        '{}', '{}'
        )
        """.format(str(Id), str(Name)))
    pass


def Add_User(UserId, UserName, Role, Password):
    with sql.connect(data_path) as conn:
        conn.execute("""
                insert into User
                values
                (%s,%s,%d,%s)
            """ % (quote(UserId), UserName, Role, quote(Password)))


def FetchAllBooks():
    res = None
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
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
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
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
