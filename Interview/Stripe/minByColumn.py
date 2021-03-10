'''
PART 1: minByColumn(table, "a") -> return {a:1, b:2, c:3}
Print the entire row where given column value is minimum
'''

from functools import *
def minByColumn(table:list, col:str) -> dict:
    if not table:
        return table
    return reduce(lambda row1, row2: row1 if (row1[col] if col in row1 else 0) <= (row2[col] if col in row2 else 0) else row2, table)

'''PART 2: minByColumnSorted(table, "a") -> return {'a':1, 'b':2, 'c':3}
Sort multiple columns, sort a column if it is identical move to next column'''
def minByColumnSorting(table:list, columns:list) -> dict:
    def helper(row1, row2):
        nonlocal columns
        for col in columns:
            row1Val = row1[col] if col in row1 else 0
            row2Val = row2[col] if col in row2 else 0
            if row1Val == row2Val:
                continue
            elif row1Val < row2Val:
                return row1
            else:
                return row2

    return reduce(helper, table)

def minByColumnSorted2(mat, cols):
    choices = list(range(len(mat)))
    for col in cols:
        vals = [(i, mat[i].get(col, 0)) for i in choices]
        _, minVal = min(vals, key = lambda x : x[1])
        choices = [i for i,val in vals if val==minVal]
        # if we find a unique minimum
        if len(choices) == 1:
            return mat[choices[0]]
    # we never found a unique minimum, so we can choose any one of them
    return mat[choices[0]]

table = [{'a':1, 'b':2, 'c':3}, {'a':10}, {'a': 1, 'b': 9, 'c':-9}]
table1 = [{}]
table2 = [
{ 'x' : 1, 'y' : 2, 'z' : 3},
{ 'x' : 1, 'y' : 2, 'z' : 2},
{'x' : 1, 'y' : 2, 'z' : 4 }
]
col = 'c'
columns = ['x', 'y', 'z']
print (minByColumn(table1, col))
print (minByColumnSorting(table2, columns))
print (minByColumnSorted2(table2, columns))