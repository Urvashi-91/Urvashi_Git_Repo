<<<<<<< HEAD
def restoreNumbersofCircle(arr):
    adj_list = {}
    result = []
    for i,j in enumerate(arr):
        print(j[0],j[1])
        adj_list[j[0]] = j[1]
        adj_list[j[1]] = j[0]
    print(adj_list)
    temp = 0
    num = arr[0][0]
    while num in adj_list:
        result.append(adj_list[num])
        temp = adj_list[num]
        del adj_list[num]
        num = temp
        
    print(result)
arr = [[3,5],[1,4],[2,4],[1,5],[2,3]]
=======
def restoreNumbersofCircle(arr):
    adj_list = {}
    result = []
    for i,j in enumerate(arr):
        print(j[0],j[1])
        adj_list[j[0]] = j[1]
        adj_list[j[1]] = j[0]
    print(adj_list)
    temp = 0
    num = arr[0][0]
    while num in adj_list:
        result.append(adj_list[num])
        temp = adj_list[num]
        del adj_list[num]
        num = temp
        
    print(result)
arr = [[3,5],[1,4],[2,4],[1,5],[2,3]]
>>>>>>> 6a511d70a9044aa21ff457120200837581634c3b
restoreNumbersofCircle(arr)