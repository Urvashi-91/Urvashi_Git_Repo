<<<<<<< HEAD
def f(a):
    count = 0
    for i in range(1, len(a)-1):
        if a[i-1] == a[i] == a[i+1]:
            continue
        elif a[i-1] == a[i] or a[i] == a[i+1] or a[i-1] == a[i+1]:
            count += 1
    print(count)

a = [1,1,2,1,2,1,1]
=======
def f(a):
    count = 0
    for i in range(1, len(a)-1):
        if a[i-1] == a[i] == a[i+1]:
            continue
        elif a[i-1] == a[i] or a[i] == a[i+1] or a[i-1] == a[i+1]:
            count += 1
    print(count)

a = [1,1,2,1,2,1,1]
>>>>>>> 6a511d70a9044aa21ff457120200837581634c3b
f(a)