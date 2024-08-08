class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1

        while len(ans) < rows * cols:
            for d in directions:
                for _ in range(steps):
                    rStart += d[0]
                    cStart += d[1]

                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        ans.append([rStart, cStart])

                if d == directions[1] or d == directions[3]:
                    steps += 1

        return ans