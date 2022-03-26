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
        print(res)
    return res


def Query_BookInfo(BookId):
    pass

