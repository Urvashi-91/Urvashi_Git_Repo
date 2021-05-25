# Python code for swapping given bits of a number
def swapBits(n, p1, p2):

# left-shift 1 p1 and p2 times
# and using XOR
n ^= 1 << p1
n ^= 1 << p2
return n

# Driver Code
print("Result =",swapBits(28, 0, 3))

# This code is contributed by rag2127

'''
Swap numbers without using thrid vairable
'''
x = 10
y = 5

# Code to swap 'x' and 'y'

# x now becomes 15
x = x + y

# y becomes 10
y = x - y

# x becomes 5
x = x - y
print("After Swapping: x =", x, " y =", y)

# This code is contributed
# by Sumit Sudhakar

'''
Swap using XOR
'''
# Python3 code to swap using XOR

x = 10
y = 5

# Code to swap 'x' and 'y'
x = x ^ y; # x now becomes 15 (1111)
y = x ^ y; # y becomes 10 (1010)
x = x ^ y; # x becomes 5 (0101)

print ("After Swapping: x = ", x, " y =", y)

# This code is contributed by
# Sumit Sudhakar

def swap(xp, yp):

	xp[0] = xp[0] ^ yp[0]
	yp[0] = xp[0] ^ yp[0]
	xp[0] = xp[0] ^ yp[0]


# Driver code
x = [10]
swap(x, x)
print("After swap(&x, &x): x = ", x[0])

# This code is contributed by SHUBHAMSINGH10

