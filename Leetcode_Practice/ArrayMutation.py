def mutateTheArray(n, a):
    b = [0]*(n)
    j = 0
    for i in range(n):
        if (i-1 < 0):
            b[j] = 0 + a[i] + a[i+1]
            j += 1
        elif (i+1 >= n):
            b[i] = a[i-1] + a[i] + 0
            j +=1
        else:
            b[i] = a[i-1] + a[i] + a[i+1]
            j += 1
    print (b)
mutateTheArray(5, [4, 0, 1, -2, 3])        