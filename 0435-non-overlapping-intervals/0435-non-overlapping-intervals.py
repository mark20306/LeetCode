class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        newEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < newEnd:
                ans += 1
                newEnd = min(newEnd, intervals[i][1])
            else:
                newEnd = intervals[i][1]
        return ans