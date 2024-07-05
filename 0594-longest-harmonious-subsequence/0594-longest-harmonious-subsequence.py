class Solution:
    def findLHS(self, nums: List[int]) -> int:
        array = sorted(nums)
        ans = 0
        l, r = 0, 1
        for i in range(len(array) - 1):
            while r < len(array) and array[r] - array[l] <= 1:
                if array[r] - array[l] == 1:
                    ans = max(ans, r - l + 1)
                r += 1
            l += 1
            r = l + 1

        return ans
