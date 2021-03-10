'''
Method1
Time Complexity: O(klogN)

'''
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [((math.sqrt(pow(point[0],2) + pow(point[1],2))),point) for point in points]
        return [point for distance,point in sorted(dist)[:k]]




'''
Method2: heap
Time Complexity: O[k+n)
'''
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for point in points:
            heapq.heappush(heap, ((math.sqrt(point[0] ** 2 + point[1] ** 2)), point))
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result

'''
Method 3
'''

pq = [[-i*i -j*j, i,j]for i,j in points[:k]]
heapq.heapify(pq)
for x,y in points[k:]:
    d = x*x + y*y
    if -pq[0][0] > d:
        heapq.heappush(pq,[-d,x,y])
        heapq.heappop(pq)
return [[x,y] fpr d,x,y in pq]