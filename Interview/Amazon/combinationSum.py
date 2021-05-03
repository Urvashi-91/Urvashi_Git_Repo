'''
Combination Sum III:Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Time Complexity: O(k.9!/(9-k)!)
- Permutation of k numbers from 9 digits P(9,k)
- Each permutation to be done for k spaces k*P(9,k)
Space Complexity: O(k)
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results


'''
Combination Sum: Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Time Complexity:
Space Complexity:
'''
'''
Method 1:Backtracking
Time Complexity:
Space Complexity:
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results


'''
Method 2: DP
Let's build the unique combinations in a gradual manner;
We shall maintiaing a dictionary from sum to a set of tuples that holdes all options for unique combinations that sum up to that sum.

For 0 we need no elements to be summed, so we initialize with empty tuple.
Let's go over all sums from 1 to target inclusive:
2.1. Let's go over all candicates
2.1.1. When considering current candidate, we can utilize the previous calculated results of unique combinations for current sum subtracting current candidate; we add current candidate to the previous sum combination and sort because the order dosent matter to us.
'''
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    unique_combinations = defaultdict(set)
    unique_combinations[0].add(tuple())
    for partial_sum in range(1, target+1):
        for c in candidates:
            for prev_comb in unique_combinations[partial_sum-c]:
                unique_combinations[partial_sum].add(tuple(sorted([c] + list(prev_comb))))
    return list(unique_combinations[target])



'''
Combination Sum II: "Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations."
Time Complexity: O(2^N)
Space Complexity: O(N)
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, results):

            if remain == 0:
                # make a deep copy of the resulted combination
                results.append(list(comb))
                return

            for next_curr in range(curr, len(candidates)):

                if next_curr > curr \
                        and candidates[next_curr] == candidates[next_curr - 1]:
                    continue

                pick = candidates[next_curr]
                # optimization: skip the rest of elements starting from 'curr' index
                if remain - pick < 0:
                    break

                comb.append(pick)
                backtrack(comb, remain - pick, next_curr + 1, results)
                comb.pop()

        candidates.sort()

        comb, results = [], []
        backtrack(comb, target, 0, results)

        return results

'''
Combination Sum IV
'''
'''
Method1: Recursion
'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        result = 0
        if target == 0:
            return 1
        elif target < 0:
            return 0

        for i in range(len(nums)):
            result += self.combinationSum4(nums, target-nums[i])
        return result