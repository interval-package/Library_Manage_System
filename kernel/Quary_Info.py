import sys
import warnings

from DataLoader import DataBaseAct, sql, data_path, quote


def Query_UserRentingHis(user_id):
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                    select Book.BookId, Book.BookName, Book.Stock, Book.Price, BookType.TypeName
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
                order by times""")
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Add_User(UserId, UserName, Role, Password):
    with sql.connect(data_path) as conn:
        conn.execute("""
                insert into User
                values
                (%s,%s,%d,%s)
            """ % (quote(UserId), UserName, Role, quote(Password)))


def Query_BookType():
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select TypeName
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


def Query_Rent(UserId, BookId):
    with sql.connect(data_path) as conn:
        conn.execute("""
            insert into RentHistory
            values
            ({0},{1},date('now'),null)
            """.format(quote(UserId), quote(BookId)))
    pass
