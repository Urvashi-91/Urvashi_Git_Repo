'''
TC: O(N+N∗logK).
SC: O(N)
'''


class Solution:

    ## using counter

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        c = Counter(words)
        arr = []

        return [x for x, y in c.most_common(k)]

    ##using heap
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = [(-val, word) for word, val in Counter(words).items()]

        heapq.heapify(c)
        arr = []

        while k:
            temp = heapq.heappop(c)
            arr.append(temp[1])
            k -= 1

        return arr