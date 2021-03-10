class Solution:
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):

            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return i, j
        '''Time complexity: O(n^2), Space complexity: O(1)'''

    def twoSumFixedX(self, nums: List[int], target: int) -> List[int]:
        reversed_map = {} # val : index

        for i, x in enumerate(nums):

            y = target - x

            if y in reversed_map:

                return [reversed_map[y], i]
            reversed_map[x] = i



