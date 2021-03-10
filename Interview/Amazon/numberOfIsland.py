class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()  # q.popright() for DFS
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ((r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands

'''
My solution involves making a set of all "1"s, and then removing all neighboring "1"s of the first one in the set in a while loop. It's quick but takes a bit more space.
Seems to me like the least amount of time it could be done in, although the space complexity is a little higher.
'''

from queue import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ones = set((i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "1")
        islands = 0
        while ones:
            islands += 1
            q = deque([next(iter(ones))])
            while q:
                one = q.pop()
                if one in ones:
                    ones.remove(one)
                    i, j = one
                    q.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])

        return islands