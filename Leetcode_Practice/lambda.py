from functools import *
def square (num):
    return num*num
square_lambda = lambda num: num*num

assert square(4) == square_lambda(4)

'''
Lambda allows only 1 expression
lambda doesnt have a name
Assertion throws error if the above expression is False'''

domain = [1,2,3,4,5]
#f(x) = x * 2
our_range = map(lambda num: num*2, domain)
print(list(our_range))
'''
map has same range as domain
map can be used instead of for loop
Syntax: map(function, iter), each item in iter is passed to the function'''
evens =  filter(lambda num: num % 2 == 0, domain)
print (list(evens))

'''
filter method filters given iterable with the help of a function that tests each element to be True or False
Syntax: filter (function, iterable)'''

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)
'''
reduce implements folding or reduction mathematical technique, it first applies
 a function on the first two items in an iterable then use the result to apply 
 with the third item in the iterable. Repeat untill iterable is exhausted
syntax: functools.reduce(function, iterable[, initialiser])'''

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print ("Sorting done by default")
print (sorted(words))
print("Sorting with a lmbda key")
print (sorted(words, key=lambda s: s.lower()))
print("Sorting with a method")
words.sort(key=str.lower, reverse=True)
'''
sorted(iterable, key=None, reverse=False)
reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.'''


#Another sort example
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]
sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list)

def greeter(prefix):
    def greet(name):
        print(f"{prefix}" + " Miss " + f"{name}")
    return greet
hello = greeter("Hello,")
goodbye = greeter("GoodBye,")
hello("Urvashi")
goodbye("Singh")

'''
Function defined inside function is a nested function, 
Hello and GoodBye gets attached to the code is called closure in Python.'''








