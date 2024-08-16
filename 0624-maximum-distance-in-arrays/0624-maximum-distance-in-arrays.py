class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curMin, curMax = arrays[0][0], arrays[0][-1]
        ans = 0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            ans = max(ans, max(arr[-1] - curMin, curMax - arr[0]))
            curMin = min(curMin, arr[0])
            curMax = max(curMax, arr[-1])
        return ans