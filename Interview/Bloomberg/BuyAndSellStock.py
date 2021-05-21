'''
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

TC: O(N)
SC: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif (prices[i] - minprice) > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit

'''
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

TC: O(N)
SC: O(1)
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1, len(prices)):
            if (prices[i] > prices[i - 1]):
                maxprofit += (prices[i] - prices[i - 1])
        return maxprofit

'''
'''
#Method1: State Track
#TC: O(N), SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        s1, s2, s3, s4 = float('inf'), 0, float('inf'), 0
        for p in prices:
            s1 = min(s1, p)
            s2 = max(s2, p - s1)
            s3 = min(s3, p - s2)
            s4 = max(s4, p - s3)
        return s4

#Method2: DP
#TC; O(N) SC: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0 for _ in range(len(prices))]
        for t in range(1, 2 + 1):
            pos = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit
        return profit
'''
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

TC: O(N)
SC:O(1)
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        Hold = [0 for _ in range(len(prices) + 1)]
        Nohold = [0 for _ in range(len(prices) + 1)]

        Hold[1] = -prices[0]
        Nohold[1] = 0

        for i in range(1, len(prices)):
            Hold[i + 1] = max(Hold[i], Nohold[i - 1] - prices[i])
            Nohold[i + 1] = max(Nohold[i], Hold[i] + prices[i])
        return Nohold[-1]

#Method2: Intuitive
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(prices) - 1:
                return 0
            ans = 0
            if i in dp:
                return dp[i]
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    ans = max(ans, prices[j] - prices[i] + dfs(j + 2))
            ans = max(ans, dfs(i + 1))
            dp[i] = ans
            return ans
        return dfs(0)
