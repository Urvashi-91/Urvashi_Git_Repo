def diff_array(arrA, arrB):
    #res1 = list (set(arrA) - set(arrB))
    #res2 = list (set(arrB) - set(arrA))
    #print (res1 + res2)
    print (list(set(arrA) ^ set(arrB)))



a = [1,2,3,4]
b = [3,4,5,6,2,2]
diff_array(a,b)