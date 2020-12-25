<<<<<<< HEAD
# Python program to check if there is Pythagorean 
# triplet in given array 
  
# Returns true if there is Pythagorean 
# triplet in ar[0..n-1] 
  
# def isTriplet(ar, n): 
#          
#     for i in range(n - 2): 
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n): 
#              
#                 # Calculate square of array elements 
#                 x = ar[i]*ar[i] 
#                 y = ar[j]*ar[j] 
#                 z = ar[k]*ar[k]  
#                 if (x == y + z or y == x + z or z == x + y): 
#                     return 1
#       
#     # If we reach here, no triplet found 
#     return 0
#   
#   
# # Driver program to test above function  
# ar = [3, 1, 4, 7, 5] 
# ar_size = len(ar) 
#   
# if(isTriplet(ar, ar_size)): 
#     print("Yes") 
# else: 
#     print("No")
    
#Time Complexity O(n^3)    
    
    
# Python program that returns true if there is  
# a Pythagorean Triplet in a given array. 
  
# Returns true if there is Pythagorean 
# triplet in ar[0..n-1] 
# def isTriplet(ar, n):
#     b = []
#     # Square all the elemennts 
#     for i in range(n): 
#         ar[i] = ar[i] * ar[i] 
#   
#     # sort array elements 
#     ar.sort() 
#   
#     # fix one element 
#     # and find other two 
#     # i goes from n - 1 to 2 
#     for i in range(n-1, 1, -1): 
#         # start two index variables from  
#         # two corners of the array and  
#         # move them toward each other 
#         j = 0
#         k = i - 1
#         while (j < k): 
#             # A triplet found 
#             if (ar[j] + ar[k] == ar[i]): 
#                 b.append(1)
#                 return True
#             else: 
#                 if (ar[j] + ar[k] < ar[i]): 
#                     j = j + 1
#                     b.append(0)
#                 else: 
#                     k = k - 1
#                     b.append(0)
#     print (b)   
#     # If we reach here, then no triplet found 
#     return False
#   
# # Driver program to test above function */ 
# ar = [3, 1, 4, 6, 5] 
# ar_size = len(ar) 
# if(isTriplet(ar, ar_size)): 
#     print("Yes") 
# else: 
#     print("No")
    


# # Function to check if the 
# # Pythagorean triplet exists or not 
# import math 
#   
# # def checkTriplet(arr, n): 
# #     maximum = 0
# #   
# #     # Find the maximum element 
# #     for i in range(n): 
# #         maximum = max(maximum, arr[i]) 
# #   
# #     # Hashing array 
# #     hash = [0]*(maximum+1) 
# #   
# #     # Increase the count of array elements 
# #     # in hash table 
# #     for i in range(n): 
# #         hash[arr[i]] += 1
# #   
# #         # Iterate for all possible a 
# #     for i in range(1, maximum+1): 
# #         # If a is not there 
# #         if (hash[i] == 0): 
# #             continue
# #   
# #         # Iterate for all possible b 
# #         for j in range(1, maximum+1): 
# #             # If a and b are same and there is only one a 
# #             # or if there is no b in original array 
# #             if ((i == j and hash[i] == 1) or hash[j] == 0): 
# #                 continue
# #   
# #             # Find c 
# #             val = int(math.sqrt(i * i + j * j)) 
# #   
# #             # If c^2 is not a perfect square 
# #             if ((val * val) != (i * i + j * j)): 
# #                 continue
# #   
# #             # If c exceeds the maximum value 
# #             if (val > maximum): 
# #                 continue
# #   
# #             # If there exists c in the original array, 
# #             # we have the triplet 
# #             if (hash[val]): 
# #                 return True
# #     return False
#   
#   
# # Driver Code 
# arr = [3, 2, 4, 6, 5] 
# n = len(arr) 
# if (checkTriplet(arr, n)): 
#     print("Yes") 
# else: 
#     print("No")


#Find Pythogorean triplet
# def find_triplet(a):
#     res=[]
#     for i in range(0, len(a)-2):
#         if a[i]**2 + a[i+1]**2 == a[i+2]**2:
#             res.append(1)
#         elif a[i]**2 + a[i+2]**2 == a[i+1]**2:
#             res.append(1)
#         elif a[i+1]**2 + a[i+2]**2 == a[i]**2:
#             res.append(1)
#         else:
#             res.append(0)
#     print(res)
#     
# a = [0,5,5,0,5,13,12]
# find_triplet(a)

def tripleSquareSum(a):
    res=[]
    for i in range(len(a)):
        a[i] = a[i] * a[i]
    # a.sort()
    for i in range(len(a)-2):
        if (a[i] + a[i+1] == a[i+2]):
            res.append(1)
        elif (a[i] + a[i+2] == a[i+1]):
            res.append(1)
        elif (a[i+1] +a[i+2] == a[i]):
            res.append(1)
        else:
            res.append(0)
    print(res)
    print(a)
a = [0,5,5,0,5,13,12]
tripleSquareSum(a)
=======
# Python program to check if there is Pythagorean 
# triplet in given array 
  
# Returns true if there is Pythagorean 
# triplet in ar[0..n-1] 
  
# def isTriplet(ar, n): 
#          
#     for i in range(n - 2): 
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n): 
#              
#                 # Calculate square of array elements 
#                 x = ar[i]*ar[i] 
#                 y = ar[j]*ar[j] 
#                 z = ar[k]*ar[k]  
#                 if (x == y + z or y == x + z or z == x + y): 
#                     return 1
#       
#     # If we reach here, no triplet found 
#     return 0
#   
#   
# # Driver program to test above function  
# ar = [3, 1, 4, 7, 5] 
# ar_size = len(ar) 
#   
# if(isTriplet(ar, ar_size)): 
#     print("Yes") 
# else: 
#     print("No")
    
#Time Complexity O(n^3)    
    
    
# Python program that returns true if there is  
# a Pythagorean Triplet in a given array. 
  
# Returns true if there is Pythagorean 
# triplet in ar[0..n-1] 
# def isTriplet(ar, n):
#     b = []
#     # Square all the elemennts 
#     for i in range(n): 
#         ar[i] = ar[i] * ar[i] 
#   
#     # sort array elements 
#     ar.sort() 
#   
#     # fix one element 
#     # and find other two 
#     # i goes from n - 1 to 2 
#     for i in range(n-1, 1, -1): 
#         # start two index variables from  
#         # two corners of the array and  
#         # move them toward each other 
#         j = 0
#         k = i - 1
#         while (j < k): 
#             # A triplet found 
#             if (ar[j] + ar[k] == ar[i]): 
#                 b.append(1)
#                 return True
#             else: 
#                 if (ar[j] + ar[k] < ar[i]): 
#                     j = j + 1
#                     b.append(0)
#                 else: 
#                     k = k - 1
#                     b.append(0)
#     print (b)   
#     # If we reach here, then no triplet found 
#     return False
#   
# # Driver program to test above function */ 
# ar = [3, 1, 4, 6, 5] 
# ar_size = len(ar) 
# if(isTriplet(ar, ar_size)): 
#     print("Yes") 
# else: 
#     print("No")
    


# # Function to check if the 
# # Pythagorean triplet exists or not 
# import math 
#   
# # def checkTriplet(arr, n): 
# #     maximum = 0
# #   
# #     # Find the maximum element 
# #     for i in range(n): 
# #         maximum = max(maximum, arr[i]) 
# #   
# #     # Hashing array 
# #     hash = [0]*(maximum+1) 
# #   
# #     # Increase the count of array elements 
# #     # in hash table 
# #     for i in range(n): 
# #         hash[arr[i]] += 1
# #   
# #         # Iterate for all possible a 
# #     for i in range(1, maximum+1): 
# #         # If a is not there 
# #         if (hash[i] == 0): 
# #             continue
# #   
# #         # Iterate for all possible b 
# #         for j in range(1, maximum+1): 
# #             # If a and b are same and there is only one a 
# #             # or if there is no b in original array 
# #             if ((i == j and hash[i] == 1) or hash[j] == 0): 
# #                 continue
# #   
# #             # Find c 
# #             val = int(math.sqrt(i * i + j * j)) 
# #   
# #             # If c^2 is not a perfect square 
# #             if ((val * val) != (i * i + j * j)): 
# #                 continue
# #   
# #             # If c exceeds the maximum value 
# #             if (val > maximum): 
# #                 continue
# #   
# #             # If there exists c in the original array, 
# #             # we have the triplet 
# #             if (hash[val]): 
# #                 return True
# #     return False
#   
#   
# # Driver Code 
# arr = [3, 2, 4, 6, 5] 
# n = len(arr) 
# if (checkTriplet(arr, n)): 
#     print("Yes") 
# else: 
#     print("No")


#Find Pythogorean triplet
# def find_triplet(a):
#     res=[]
#     for i in range(0, len(a)-2):
#         if a[i]**2 + a[i+1]**2 == a[i+2]**2:
#             res.append(1)
#         elif a[i]**2 + a[i+2]**2 == a[i+1]**2:
#             res.append(1)
#         elif a[i+1]**2 + a[i+2]**2 == a[i]**2:
#             res.append(1)
#         else:
#             res.append(0)
#     print(res)
#     
# a = [0,5,5,0,5,13,12]
# find_triplet(a)

def tripleSquareSum(a):
    res=[]
    for i in range(len(a)):
        a[i] = a[i] * a[i]
    # a.sort()
    for i in range(len(a)-2):
        if (a[i] + a[i+1] == a[i+2]):
            res.append(1)
        elif (a[i] + a[i+2] == a[i+1]):
            res.append(1)
        elif (a[i+1] +a[i+2] == a[i]):
            res.append(1)
        else:
            res.append(0)
    print(res)
    print(a)
a = [0,5,5,0,5,13,12]
tripleSquareSum(a)
>>>>>>> 6a511d70a9044aa21ff457120200837581634c3b
