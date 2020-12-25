import re

# Split the string at every white-space character:

# txt = "The rain in Spain"
# x = re.split('\s', txt)
# print(x)
# n = len(x)
# print(n)
x = ['TRWS', 'WTFG']
p = {"2": ['T','F','R'], "3": "WGS"}
def phone(x,p):
    n = len(x)
    for i in range(n):
        y = re.findall('[a-zA-z]', x[i])
        for j in range(4):
            temp = y[j]
            z = (k for k, v in p.items() if v == temp)
            print (p[z])
phone(x,p)
