from collections import deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        sortedWords = []
        if len(words) <= 0:
            return ""

        '''["wrt","wrf","er","ett","rftt"]'''

        # initialisation
        inDegree = {character: 0 for word in words for character in word}
        graph = {character: [] for word in words for character in word}

        # graph building
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            diff = False
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    diff = True
                    parent, child = w1[j], w2[j]
                    graph[parent].append(child)
                    inDegree[child] += 1
                    break
            if not diff and len(w1) > len(w2):
                return ""

        # Build Source
        source = deque()
        for vertex in inDegree:
            if inDegree[vertex] == 0:
                source.append(vertex)

        while source:
            vertex = source.popleft()
            sortedWords.append(vertex)
            for character in graph[vertex]:
                inDegree[character] -= 1
                if inDegree[character] == 0:
                    source.append(character)

        if len(sortedWords) != len(inDegree):
            return ""

        return ''.join(sortedWords)


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
