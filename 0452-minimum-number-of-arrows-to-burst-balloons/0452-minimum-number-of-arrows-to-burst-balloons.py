class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = len(points)
        points.sort()
        newRange = points[0]
        for i in range(1, len(points)):
            if points[i][0] <= newRange[1]:
                ans -= 1
                newRange = [points[i][0], min(newRange[1], points[i][1])]
            else:
                newRange = [points[i][0], points[i][1]]
        return ans
