'''
Method1: Brute Force
Time Complexity: O(n^2)
Space complexity: O(1)
'''


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # 60,120,180,240

        pair = 0
        # 20+150 = 170%60
        for i in range(len(time) - 1):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    pair += 1
        return pair


'''
Method2: One Pass
Time Complexity: O(n)
Space Complexity: O(1)
'''


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        (a+b)%60 == 0
        a%60 + b%60 == 60'''

        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0:
                ret += remainders[0]
            else:
                ret += remainders[60 - t % 60]
            remainders[t % 60] += 1
        return ret
