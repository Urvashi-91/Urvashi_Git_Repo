'''
Given a balanced string containing letters a-z and brackets "()[]{}",
return the deepest nested substrings
Example: "a[bc]def{cd}" -> ["bc","cd"]
'''

'''
Deepest Nested paranthesis depth
https://www.geeksforgeeks.org/find-maximum-depth-nested-parenthesis-string/
'''
# A Python program to find the maximum depth of nested
# parenthesis in a given expression

# function takes a string and returns the
# maximum depth nested parenthesis
def maxDepth(S):
	current_max = 0
	max = 0
	n = len(S)

	# Traverse the input string
	for i in range(n):
		if S[i] == '(':
			current_max += 1

			if current_max > max:
				max = current_max
		elif S[i] == ')':
			if current_max > 0:
				current_max -= 1
			else:
				return -1

	# finally check for unbalanced string
	if current_max != 0:
		return -1

	return max

# Driver program
s = "( ((X)) (((Y))) )"
print (maxDepth(s))

# This code is contributed by BHAVYA JAIN

