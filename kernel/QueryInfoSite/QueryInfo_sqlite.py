from kernel.QueryInfoSite.DataLoader import sql, data_path, quote
from kernel.QueryInfoSite.ExceptionClasses_Query import *
import pandas as pd


def connGetter():
    return sql.connect(data_path)


def connAction(conn, command):
    cursor = conn.execute(command)
    return cursor
