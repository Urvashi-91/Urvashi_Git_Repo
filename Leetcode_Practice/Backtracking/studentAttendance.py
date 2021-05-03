'''
A school punishes students if they are absent more than once per term,
or if they are ever late 3 days in a row. Accordingly, every day,
for each student, the school records a single letter:
'A' for absent,
'O' for on time, and
'L' for late.
For example: "LAOLL" (Here, the student is not in trouble
because there is only one absence, and although there are 3 late days, they are not consecutive.)

Write a program that returns the number of strings of length 30
for which the student is in good standing.
'''

from itertools import *
import re
def checkRecord(n):
    all_comb = []
    count = 0
    comb = list(combinations_with_replacement('ALP', n))
    for c in comb:
        permute = list(permutations(c, n))

        for p in permute:
            string = ""
            for ele in p:
                string += ele
            if string not in all_comb:
                all_comb.append(string)

    for record in all_comb:
        if re.findall('LLL', record) or len(re.findall('A', record)) >= 2:
            count += 1
    print (len(all_comb) - count)

checkRecord(2)


'''
DP: Top-Down 
'''
from itertools import *
import re


class Solution:
    def checkRecord(self, n: int) -> int:
        M = 1000000007

        @cache
        def dfs(n, cons_L, has_A):

            if n == 0:
                return 1
            tmp = 0
            # if (n,cons_L,has_A) in cache:
            #     return cache[n,cons_L,has_A]
            if not has_A:
                tmp += dfs(n - 1, 0, True)
                tmp %= M
            if cons_L < 2:
                tmp += dfs(n - 1, cons_L + 1, has_A)
                tmp %= M
            tmp += dfs(n - 1, 0, has_A)
            tmp %= M

            # cache[n,cons_L,has_A] = tmp
            return tmp

        return dfs(n, 0, False)


'''
Bottom Up Approach
'''
from itertools import *
import re


class Solution:
    def checkRecord(self, n: int) -> int:
        M = 1000000007

        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n + 1)]
        # Base Cases
        dp[1][0][0] = 1
        dp[1][0][1] = 1
        dp[1][1][0] = 1
        dp[1][1][1] = 0
        dp[1][2][0] = 0
        dp[1][2][1] = 0
        for i in range(2, n + 1):
            dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][1][0] + dp[i - 1][2][0]) % M  # no A
            dp[i][0][1] = dp[i][0][0] + (dp[i - 1][0][1] + dp[i - 1][1][1] + dp[i - 1][2][1]) % M  # one A
            dp[i][1][0] = dp[i - 1][0][0] % M
            dp[i][1][1] = dp[i - 1][0][1] % M
            dp[i][2][0] = dp[i - 1][1][0] % M
            dp[i][2][1] = dp[i - 1][1][1] % M
        total = 0
        for i in range(3):
            for j in range(2):
                total += dp[-1][i][j]
                total %= M
        return total
