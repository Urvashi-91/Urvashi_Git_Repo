from collections import defaultdict
def minByCol(table:list, col_name:str) -> dict:
    col = set()
    for row in table:
        if col_name in row:
            col.add(row[col_name])

        else:
            row[col_name] = 0
            col.add(row[col_name])

    print (min(col))


def sortByCol(table:list, col_name:str) -> dict:








table = [{"a":1, "b":2, "c":3, "d":5}, {"a":10, "d":1}, {"a": 2,"d": 9}]
col_name = "d"
minByCol(table, col_name)