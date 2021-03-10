Q1: Imagine you have 3 denomination of currencies (4, 6 and 11)
And you are given a target number.
Write a function that checks whether the given target is achievable via the denominations
You can use a single denomination multiple times.
I : 31
O : true
I : 9
O : false

Q2: Write a function to transform input set to output set
I : {5}
O : {5}
I : {5, 6}
O : {5, 6 , 30}
I : {5, 6, 8}
O : {5, 6, 8, 30, 40, 48, 240}


'''
For the iterative solution, we think in bottom-up manner. Before calculating 
F
(
i
)
F(i), we have to compute all minimum counts for amounts up to 
i
i. On each iteration 
i
i of the algorithm 
F
(
i
)
F(i) is computed as 
min
⁡
j
=
0
…
n
−
1
F
(
i
−
c
j
)
+
1
min 
j=0…n−1
​	
 F(i−c 
j
​	
 )+1
n the example above you can see that:

F
(
3
)
=
min
⁡
{
F
(
3
−
c
1
)
,
F
(
3
−
c
2
)
,
F
(
3
−
c
3
)
}
+
1
=
min
⁡
{
F
(
3
−
1
)
,
F
(
3
−
2
)
,
F
(
3
−
3
)
}
+
1
=
min
⁡
{
F
(
2
)
,
F
(
1
)
,
F
(
0
)
}
+
1
=
min
⁡
{
1
,
1
,
0
}
+
1
=
1
  
F(3)
​	
  
=min{F(3−c 
1
​	
 ),F(3−c 
2
​	
 ),F(3−c 
3
​	
 )}+1
=min{F(3−1),F(3−2),F(3−3)}+1
=min{F(2),F(1),F(0)}+1
=min{1,1,0}+1
=1
​	
  '''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

'''zbfs
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        BFS solution
        '''
        if amount == 0:
            return 0

        seen = set()

        from collections import deque
        q = deque([[0, 0]])

        while q:
            curr, level = q.popleft()

            if level != 0 and curr == amount:
                return level

            for c in coins:
                if curr + c not in seen and curr + c <= amount:
                    q.append([curr + c, level + 1])
                    seen.add(curr + c)
        return -1



'''
'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]

