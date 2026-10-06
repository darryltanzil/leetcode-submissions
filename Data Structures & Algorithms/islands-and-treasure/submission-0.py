from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        seen = set()

        def addCell(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and not grid[r][c] == -1 and not (r, c) in seen:
                seen.add((r, c))
                q.append([r, c])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r, c])
                    seen.add((r, c))

        dist = 0
        while q:
            # for every level
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for x, y in [[r+1, c], [r-1, c], [r,c+1], [r, c-1]]:
                    addCell(x, y)
            dist += 1
                