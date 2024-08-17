class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        prevRow = points[0]

        for r in range(1, rows):
            left, right = [0] * cols, [0] * cols

            left[0] = prevRow[0]
            for c in range(1, cols):
                left[c] = max(prevRow[c], left[c - 1] - 1)

            right[cols - 1] = prevRow[cols - 1]
            for c in range(cols - 2, -1, -1):
                right[c] = max(prevRow[c], right[c + 1] - 1)

            currRow = [0] * cols
            for j in range(len(currRow)):
                currRow[j] = points[r][j] + max(left[j], right[j])
            
            prevRow = currRow
        
        return max(prevRow)
