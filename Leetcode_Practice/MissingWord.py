s = "I like my Pichi"
t = "I Pichi"
a = s.split()
b = t.split()
m = []
if len(a) == len(b):
    print("No missing word")
else:
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            print(a[i])
