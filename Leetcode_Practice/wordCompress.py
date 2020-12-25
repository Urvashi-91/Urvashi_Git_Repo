# from itertools import groupby
# import re
# # def compress(string):
# #     return re.sub(r'(?<![0-9])[1](?![0-9])', '', ''.join('%s%s' % (char, sum(1 for _ in group)) for char, group in groupby(string)))
# # s = compress('aaabccddd')
# # print (s)
# s = 'aaabccdddaaa'
# for char, group in groupby(s):
#     print (char, len(list(group)))
#     if len(list(group)) == 3:
#         s.drop(index='group')
# print (s)
#
# str_new = s.groupby(s).filter

# from itertools import groupby as df
# s = 'aaabdddcaaa'
# df.
# print (df.groupby(s).groups)

# from collections import Counter
# def string_compression(string):
#     counter = Counter(string)
#     result = ''
#     for k, v in counter.items():
#         if v == 3:
#             continue
#         else:
#             result = result + k*v
#     print(result)
# string_compression('aaabccddd')

s = 'aaabccddd'
# result = {}
import itertools
result = []
for (key,group) in itertools.groupby(s):
    print (type(key,group))
#     print (key,list(group))
#     if len(list(group)) == 3:
#         result.append(next(key))
#     else:
#         result.append(key)
#     if key*3 == s[:3]:
#         continue
#
#     else:
#         result.append(s[:3])
# print (result)



