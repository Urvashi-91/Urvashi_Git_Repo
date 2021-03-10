'''
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''

def is_dict(var):
    return str(type(var)) == "<class 'dict'>"


def flatten_helper(d, flat_d, path):
    if not is_dict(d):
        flat_d[path] = d
        return

    for key in d:
        new_keypath = "{}.{}".format(path, key) if path else key
        flatten_helper(d[key], flat_d, new_keypath)


def flatten(d):
    flat_d = dict()
    flatten_helper(d, flat_d, "")
    return flat_d


# Tests

d = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

assert flatten(d) == {
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}