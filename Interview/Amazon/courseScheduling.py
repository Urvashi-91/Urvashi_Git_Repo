from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedgraph = []
        if numCourses <= 0:
            return False

        inDegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        # Build graph
        for prereq in prerequisites:
            parent = prereq[0]
            child = prereq[1]
            graph[parent].append(child)
            inDegree[child] += 1

        # sources
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sortedgraph.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        return len(sortedgraph) == numCourses

