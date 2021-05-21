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


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_dict = Counter(words)
        # words_dict = {}
        # for word in words:
        #    if word not in words_dict:
        #        words_dict[word] = 0
        #    words_dict[word] += 1

        return list(sorted(words_dict.keys(), key=lambda x: (-words_dict[x], x)))[:k]

'''
TC: O(nlogk)
SC: O(k)
'''
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = (heapq.nsmallest(k, count.items(), key= lambda item: (-item[1], item[0])))
        return [word for word, _ in heap]