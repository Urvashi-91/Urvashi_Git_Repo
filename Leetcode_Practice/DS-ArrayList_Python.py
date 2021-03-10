from array import *
def arrayList(number):
    array1 = array('i', [3])
    array1.insert(1, number)
    for x in array1:
        print(x)

arrayList(5)
''' Arrays are used for numeric datatypes'''

def stringList(word):
    array1 = ['word1']
    array1.append(word)
    print(array1)

stringList('word2')

def joinWords(word):
    sentence = ""
    for k in word:
        sentence += k + " "
    print (sentence)

word = ['I', 'am', 'the', 'best', 'coder']
joinWords(word)

from collections import defaultdict
def def_value():
    return False
def isUnique(word):
    if len(word) > 256:
        return False
    if not word:
        print ('No Input')
        return False
    seen = defaultdict(def_value)
    for k in word:
        #seen[k] = False
        if seen[k] == True:
            return False
        seen[k] = True
    return True

result = isUnique("")
if result is True:
    print ('True')
else:
    print ('False')



