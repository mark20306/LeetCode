class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        count = 0
        def dfs(r, c, visit):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visit:
                return
            visit.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visit:
                    dfs(r, c, visit)
                    count += 1
        if count != 1:
            return 0
        land = list(visit)
        for r, c in land:
            grid[r][c] = 0
            visit = set()
            count = 0
            for r2 in range(rows):
                for c2 in range(cols):
                    if grid[r2][c2] and (r2, c2) not in visit:
                        dfs(r2, c2, visit)
                        count += 1
            grid[r][c] = 1
            if count != 1:
                return 1
        return 2


        
