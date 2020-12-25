# def updateTime (m,n):
#     # length_n = len(n)
#     # length_m = len(m)
#     "Assuming m and n have equal length"
#     count = 0
#     maxequal = 0
#     for i in range(len(n)):
#         if m[i] == n[i] and maxequal<m[i]:
#             maxequal = m[i]
#             count += 1
#     return count
#
# m = [1,2,3,4,1]
# n = [5,4,3,4,1]
# print (updateTime(m,n))

def diskSpace(n, space, x):
    subArray = []
    min_array = []
    i = 0
    if x == 1:
        max_value = max(space)
        return max_value
    else:
        while i < n:
            min_array.clear()
            for j in range(i, i + x):
                subArray.append(space[j])

            min_array.append(min(subArray))
            i += 1

        return (max(min_array))


print(diskSpace(5, [1, 2, 3, 1, 2], 2))
