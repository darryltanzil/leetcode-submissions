from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        seen = set()

        def addCell(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in seen and not grid[x][y] == -1:
                q.append([x, y])
                seen.add((x, y))
                
        # add all treasure chests to the queue initially
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j])
                    seen.add((i, j))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for x, y in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    addCell(x, y)
            dist += 1
            
                