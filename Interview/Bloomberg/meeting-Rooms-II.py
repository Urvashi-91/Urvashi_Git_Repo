'''
TC: O(NlognN)
SC: O(N)
Proority Queue
'''
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        minRooms = 0
        minHeap = []
        for meeting in intervals:
    # remove all the meetings that have ended
            while(len(minHeap) > 0 and meeting[0] >= minHeap[0]):
                heappop(minHeap)
    # add the current meeting into min_heap
            heappush(minHeap, meeting[1])
    # all active meetings are in the min_heap, so we need rooms for all of them.
            minRooms = max(minRooms, len(minHeap))
        return minRooms