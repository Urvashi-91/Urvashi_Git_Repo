#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
from numpy import *

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# def diagonalDifference(arr):
    # Write your code here
    prim =0
    sec=0
    # length = len(arr)
arr = [[1,2,3], [4,5,6]   
    l = arr.size
    print (l)
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][(length-count-1)]
    print abs(prim-sec)



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# 
#     n = int(input().strip())
# 
#     arr = []
# 
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
# 
#     result = diagonalDifference(arr)
# 
#     fptr.write(str(result) + '\n')
# 
#     fptr.close()
