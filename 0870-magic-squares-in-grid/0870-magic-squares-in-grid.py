class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        p1 = '438167294381672'
        p2 = '927618349276183'
        ans = 0

        def magic(r, c):
            if grid[r][c] != 5:
                return 0
            neighbors = [
                [r - 1, c - 1], [r - 1, c],
                [r - 1, c + 1], [r, c + 1],
                [r + 1, c + 1], [r + 1, c],
                [r + 1, c - 1], [r, c - 1]
            ]
            res = ''
            for dr, dc in neighbors:
                res += str(grid[dr][dc])
            if res in p1 or res in p2:
                return 1
            return 0
            
        for r in range(1, rows - 1):
            for c in range(1, cols -1):
                ans += magic(r, c)
        return ans
