'''
Method: Recursion
Time Complexity: O(2^n) here, 2 is the number of child nodes,
 and n is the number of levels of tree
'''
def fib(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

'''
Method2: DP/ Memoization Top Down approach
Time Complexity: O(N)
'''
from collections import defaultdict
def fib_memo(n):
    #Base Cases
    memory = defaultdict(lambda : 0)
    def helper(n, memory):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            if memory[n] == 0:
                memory[n] = helper(n-1, memory) + helper(n-2, memory)
        return memory[n]
    return helper(n, memory)

'''
Method 3: Bottom UP Approach
Time Complexity:
Space Complexity:
'''
from collections import defaultdict
def fib_memo_bottom(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(3,n):
            c = a + b
            a,b = b,c
        return a+b


'''
Testing
'''

def test_fib():
    assert fib(4) == 2
    assert fib_memo(4) == 2
    assert fib_memo_bottom(4) == 2

test_fib()