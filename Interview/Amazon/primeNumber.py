# A school method based Python3 program
# to check if a number is prime

# function check whether a number
# is prime or not


def isPrime(n):

	# Corner case
	if (n <= 1):
		return False

	# Check from 2 to n-1
	for i in range(2, n):
		if (n % i == 0):
			return False

	return True


# Driver Code
if isPrime(11):
	print("true")
else:
	print("false")

# This code is contributed by Sachin Bisht

'''
Recursion
'''


# Python3 program to check whether a number
# is prime or not using recursion

# Function check whether a number
# is prime or not
def isPrime(n, i):
    # Corner cases
    if (n == 0 or n == 1):
        return False

    # Checking Prime
    if (n == i):
        return True

    # Base cases
    if (n % i == 0):
        return False

    i += 1

    return isPrime(n, i)


# Driver Code
if (isPrime(35, 2)):
    print("true")
else:
    print("false")

# This code is contributed by bunnyram19

