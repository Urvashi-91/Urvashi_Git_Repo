'''
The defaultdict will automatically assign zero as the value to any key it doesn’t already have in it.
'''
from collections import defaultdict


sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)

'''
list of values
'''
from collections import defaultdict


my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)

print(d)

'''
default dict with lambda
'''
from collections import defaultdict
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print (animal['Nick'])
#Monkey

print (animal)
#defaultdict(<function <lambda> at 0x7f32f26da8c0>, {'Nick': 'Monkey', 'Sam': 'Tiger'})

