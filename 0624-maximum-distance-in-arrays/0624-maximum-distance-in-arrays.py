class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort()
        ans = 0
        for i in range(1, len(arrays)):
            temp = max(abs(arrays[i][-1] - arrays[0][0]),abs(arrays[0][-1] - arrays[i][0]))
            ans = max(ans, temp)
        return ans