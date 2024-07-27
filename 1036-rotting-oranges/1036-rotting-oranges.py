class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r, c, 0])
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue:
            row, col, minute = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    queue.append([r, c, minute + 1])
                    grid[r][c] = 2
                    fresh -= 1

        if fresh > 0:
            return -1

        return minute

