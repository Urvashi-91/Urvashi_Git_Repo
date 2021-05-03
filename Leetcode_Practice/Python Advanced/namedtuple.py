'''
A struct is basically a complex data type that groups a list of variables under one name.
namedtuple which you can use to replace Python’s tuple.
'''
from collections import namedtuple

Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine',
               cost=1200.00, amount=10)
print(auto_parts.id_num)

'''
Python dict into object
'''
from collections import namedtuple

Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', Parts.keys())(**Parts) #**(**Parts)**. The double asterisk means that we are calling our class using keyword arguments, which in this case is our dictionary.
print (parts)
#Parts(amount=10, cost=1200.0, id_num='1234', desc='Ford Engine')

'''
Same as above
'''
parts = namedtuple('Parts', Parts.keys())
print (parts)
#<class '__main__.Parts'>

auto_parts = parts(**Parts)
print (auto_parts)
#Parts(amount=10, cost=1200.0, id_num='1234', desc='Ford Engine')

