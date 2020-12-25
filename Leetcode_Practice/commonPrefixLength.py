import re
string = ['abcabcd','abcabcd','abcabcd']
def commonPrefix(string):
    k = len(string)
    length = []
    for i in range(k):
        string1 = string[i]
        n = len(string1)

        count = n
        for j in range(n):
            prefix = string1[0:j]
            suffix = string1[j:n]
            if bool(re.match(prefix,suffix)):
               # print (prefix,suffix,"item matched")
               count += len(prefix)
        length.append(count)
    print (length)
commonPrefix(string)