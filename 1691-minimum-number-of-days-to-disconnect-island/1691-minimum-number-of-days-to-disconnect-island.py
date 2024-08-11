class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visit:
                return
            visit.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit)
        
        def count_island():
            visit = set()
            count = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] and (r, c) not in visit:
                        dfs(r, c, visit)
                        count += 1
            return count
        if count_island() != 1:
            return 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                else:
                    grid[r][c] = 0
                    if count_island() != 1:
                        return 1
                    grid[r][c] = 1
        return 2


        
