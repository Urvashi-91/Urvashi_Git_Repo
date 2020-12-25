# def rectangleBoxes(operations):
# operations = [[0, 1, 3], [0, 4, 2], [1, 3, 4], [1, 3, 2]]
# j = 0
# area = []
# compare_area = []
# result = []
# for i in range(len(operations)):
#     if operations[i][0] == 0:
#         area.append(operations[i][1] * operations[i][2])
#     else:
#         compare_area.append(operations[i][1] * operations[i][2])
# for j in range(len(compare_area)):
#     if compare_area[j] >= sum(area):
#         result.append('true')
#     else:
#         result.append('false')
# print (result)

# def isZigZag(numbers):
#     result = []
#     for i in range(len(numbers)-2):
#         if numbers[i] < numbers[i+1] and numbers [i+1] > numbers[i+2]:
#             result.append(1)
#         elif numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2]:
#             result.append(1)
#         elif numbers[i:i+2] == sorted(numbers[i:i+2]):
#             result.append(0)
#         elif numbers[i:i+2] == numbers[i+2:i]:
#             result.append(0)
#         else:
#             result.append(0)
#     print (result)
#
# numbers = [1000000000,1000000000,1000000000]
# isZigZag(numbers)

# def sumOfStrings(a, b):
#     a = list(a)
#     b = list(b)
#     d = ""
#     if len(a) < len(b):
#         e = ["0"] * (len(b) - len(a))
#         e.extend(a)
#         a = e
#     elif len(a) > len(b):
#         e = ["0"] * (len(a) - len(b))
#         e.extend(b)
#         b = e
#     for i in range(len(a) - 1, -1, -1):
#         a[i] = int(a[i]) + int(b[i])
#     for j in range(len(a)):
#         d += str(a[j])
#     print(d)
#
#
# a = "100000"
# b = "9999999999"
# sumOfStrings(a, b)


# def booleanQueue(n, operations):
#     a = [0]*n
#     flag = 0
#     i = 0
#     for op in operations:
#
#         if op == 'L':
#
#             while flag == 0 and i < n:
#                 print (a[i],i)
#                 if a[i] == 0:
#                     a[i] = 1
#                     i += 1
#                     flag = 1
#                 else:
#                     i += 1
#             flag = 0
#
#         else:
#             b = list(op)
#             a[int(b[1])] = 0
#             i = 0
#     print (a)
#
# booleanQueue(2, ["L","L","L","C0","C0"])


# def isSubmatrixFull(numbers):
#     n = len(numbers[0])
#     result = []
#     x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     array = []
#     j = 0
#     for k in range(n - 2):
#         for i in range(3):
#             for j in range(k, 3 + k):
#                 array.append(numbers[i][j])
#         if sorted(array) == x:
#             result.append('true')
#             array.clear()
#         else:
#             result.append('false')
#             array.clear()
#     print(result)
#
#
# # numbers = [[1, 2, 3, 2, 5, 7,1,4,7], [4, 5, 6, 1, 7, 6,2,5,8], [7, 8, 9, 4, 8, 3,3,6,9]]
# numbers = [[1,2,3],[4,5,6],[7,8,9]]
# isSubmatrixFull(numbers)


# def findDiagonalOrder(matrix):
#     M = len(matrix)
#     N = len(matrix[0])
#     Sum = {}
#     result,inter = [],[]
#     for i in range(M):
#         for j in range(N):
#            Sum.setdefault(i+j, []).append(matrix[i][j])
#     for k in range(M+N-1):
#         if k%2 == 0:
#             print (Sum[k])
#             inter.extend(Sum[k])
#             inter.reverse()
#             result.extend(inter)
#             inter.clear()
#         else:
#             print (Sum[k])
#             result.extend(Sum[k])
#     print (Sum,result)
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# findDiagonalOrder(matrix)

# def findDiagonalOrder(matrix):
#     M = len(matrix)
#     N = len(matrix[0])
#     Sum = {}
#     result,inter = [],[]
#     for i in range(M):
#         for j in range(N):
#            Sum.setdefault(i-j, []).append(matrix[i][j])
#     for k in Sum:
#         if abs(k%2) == 0:
#             print (Sum[k])
#             inter.extend(Sum[k])
#             inter.reverse()
#             result.extend(inter)
#             inter.clear()
#         else:
#             print (Sum[k])
#             result.extend(Sum[k])
#     print (Sum,result)
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# findDiagonalOrder(matrix)

# def diagonalSort(matrix):
#     M = len(matrix)
#     N = len(matrix[0])
#     Sum = {}
#
#     for i in range(M):
#         for j in range(N):
#             Sum.setdefault(i - j, []).append(matrix[i][j])
#
#     for k in Sum:
#         Sum[k].sort(reverse=1)
#     for i in range(M):
#         for j in range(N):
#             matrix[i][j] = Sum[i-j].pop()
#     print(matrix)

# import collections
# def goodTuples(a):
#     n = len(a)
#     count,c = 0,0
#     for i in range(1,n-1):
#         l = [a[i-1],a[i],a[i+1]]
#         for items,count in collections.Counter(l).items():
#             if count == 2:
#                 c += 1
#     print (c)
#
# a = [1,1,2,1,2,1,1,6,4,5,5,5]
# goodTuples(a)

# def partition(self, s):
#     res = []
#     self.dfs(s, [], res)
#     return res
#
# def dfs(self, s, path, res):
#     if not s:
#         res.append(path)
#         return
#     for i in range(1, len(s) + 1):
#         if self.isPal(s[:i]):
#             self.dfs(s[i:], path + [s[:i]], res)
#
# def isPal(self, s):
#     return s == s[::-1]
#
# def palindromeCutting(s):
