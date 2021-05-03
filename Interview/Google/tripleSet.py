'''
Cracking The Coding Interview
Chapter 8: Recursion/DP/Memoisation
Question 8.1: "Triple Step: A child is running up a staircase
with n steps and can hop either 1 step, 2 steps, or 3 steps
at a time. Implement a method to count how many possible ways
the child can run up the stairs."
'''
'''
Method1: Recursion
'''
def countSteps(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return countSteps(n-1) + countSteps(n-2) + countSteps(n-3)


'''
Method2: Memoization
'''
from collections import defaultdict
def countSteps_Memo(n):
    memo = defaultdict(lambda:0)
    memo[0] = 1
    memo[1] = 1
    def hop(n, memo):
        if n == 0 or n == 1:
            return 1
        elif n < 0:
            return 0
        else:
            for i in range(2, n+1):
                if memo[i] == 0:
                    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]
    return hop(n, memo)

def test_countSteps():
    assert countSteps(2) == 2
    assert countSteps_Memo(2) == 2

test_countSteps()