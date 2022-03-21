import sys
import warnings

try:
    from DataLoader import DataBaseAct, sql
except ImportError:
    sys.path.append("../../")
    from DataLoader import DataBaseAct, sql


def Query_BookInfo(conn, BookId):
    with conn:
        cursor = conn.execute("""
            select * from Book
            where Book.BookId = %s
            """ % (str(BookId)))

