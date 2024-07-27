class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            row, col, steps = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.':
                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        return steps + 1
                    maze[r][c] = '+'
                    queue.append((r, c , steps + 1))
        
        return -1