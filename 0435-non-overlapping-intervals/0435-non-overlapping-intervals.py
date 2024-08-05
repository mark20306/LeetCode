class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        newEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < newEnd:
                ans += 1
                newEnd = min(newEnd, end)
            else:
                newEnd = end
        return ans