import pandas as pd
import os.path as opa
import xlwt
from kernel.QueryInfoSite.QueryInfo import Query_UserRank, Query_BookRank, FetchAllUser, FetchAllBooks


def SaveToExcel(path, sheet_name, method):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)
    tar = method()
    for i, items in zip(range(len(tar)), tar):
        for j, item in zip(range(len(items)), items):
            sheet.write(i, j, item)
    workbook.save(opa.join(path, sheet_name + '.xls'))
    pass


if __name__ == '__main__':
    pass
