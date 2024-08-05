class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = len(points)
        points.sort()
        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prev[1]:
                ans -= 1
                prev = [curr[0], min(prev[1], curr[1])]
            else:
                prev = curr
        return ans
