from functools import *
def min_by_key(col, table):
    if not table and len(table) == 1:
        return table
    elif len(table) == 0:
        return None
    else:
        return reduce(lambda row1, row2: row1 if (row1[col] if col in row1 else 0) <= (row2[col] if col in row2 else 0) else row2, table)

assert min_by_key("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
assert min_by_key("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
assert min_by_key("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
assert min_by_key("a", [{}]) == {}
assert min_by_key("b", [{"a": -1}, {"b": -1}]) == {"b": -1}
assert min_by_key("a", []) == None



def first_by_key(col, order,  table):
    if not table and len(table) == 1:
        return table
    # elif len(table) == 0:
    #     return None
    elif order == 'asc':
        return reduce(lambda row1, row2: row1 if (row1[col] if col in row1 else 0) <= (row2[col] if col in row2 else 0) else row2, table)
    elif order == 'desc':
        return reduce(lambda row1, row2: row1 if (row1[col] if col in row1 else 0) >= (row2[col] if col in row2 else 0) else row2,table)
    else:
        return None


assert first_by_key("a", "asc", [{"a": 1}]) == {"a": 1}
assert first_by_key("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [{"b": 1}, {"b": -2}]
assert first_by_key("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
assert first_by_key("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
assert first_by_key("b", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": 1}
assert first_by_key("a", "desc", [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]) == {"a": 10, "b": -10}


class RecordComparator():
    def __init__(self, key, typ):
        self.key = key
        self.typ = typ

    def compare(self, rec1, rec2):
        typOrder = {'asc': 1, 'desc': -1}
        if self.key not in rec1:
            val1 = 0
        else:
            val1 = rec1[self.key]
        if self.key not in rec2:
            val2 = 0
        else:
            val2 = rec2[self.key]
        if val1 < val2:
            return typOrder[self.typ] * -1
        elif val1 > val2:
            return typOrder[self.typ] * 1
        else:
            return 0

cmp = RecordComparator("a", "asc")
assert cmp.compare({"a": 1}, {"a": 2}) == -1
assert cmp.compare({"a": 2}, {"a": 1}) == 1
assert cmp.compare({"a": 1}, {"a": 1}) == 0