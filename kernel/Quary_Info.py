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
