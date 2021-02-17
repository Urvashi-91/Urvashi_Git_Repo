'''
collections: Container datatypes
    namedtuple():factory function for creating tuple subclasses with named fields
    deque: list-like container with fast appends and pops on either end
    ChainMap: dict-like class for creating a single view of multiple mappings
    Counter: dict subclass for counting hashable objects
    OrderedDict: dict subclass that remembers the order entries were added
    defaultdict: dict subclass that calls a factory function to supply missing values
    UserDict: wrapper around dictionary objects for easier dict subclassing
    UserList: wrapper around list objects for easier list subclassing
    UserString: wrapper around string objects for easier string subclassing
'''
import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps,'\n')

print('Keys = {}'. format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('day3 in res: {}'.format(('day3' in res)))
print('day4 in res: {}'.format(('day4' in res)))

dict2['day4'] = 'Fri'
print(res.maps,'\n')
