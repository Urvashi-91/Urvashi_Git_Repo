<<<<<<< HEAD
def concatswap(s, sizes):
    result = []
    temp = 0
    for each_size in sizes:
        temp1 = temp + each_size
        result.append(s[temp:temp1])
        temp = temp1
        
    if len(result)==1:
        return result[0]
    
    i = 0
    j = 1
    
    while(i<len(result) and j < len(result)):
        result[i], result[j] = result[j], result[i]
        i+=2
        j+=2
        
    print (''.join([ele for ele in result]))
=======
def concatswap(s, sizes):
    result = []
    temp = 0
    for each_size in sizes:
        temp1 = temp + each_size
        result.append(s[temp:temp1])
        temp = temp1
        
    if len(result)==1:
        return result[0]
    
    i = 0
    j = 1
    
    while(i<len(result) and j < len(result)):
        result[i], result[j] = result[j], result[i]
        i+=2
        j+=2
        
    print (''.join([ele for ele in result]))
>>>>>>> 6a511d70a9044aa21ff457120200837581634c3b
concatswap('descognail', [3,2,3,1,1])