class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(w)
        verticalCuts.sort()

        max_h = 0
        prev_height = 0
        for hc in horizontalCuts:
            cut_length = hc - prev_height
            max_h = max(cut_length, max_h)
            prev_height = hc

        max_w = 0
        prev_width = 0
        for vc in verticalCuts:
            cut_length = vc - prev_width
            max_w = max(cut_length, max_w)
            prev_width = vc

        return max_h * max_w % 1000000007