class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        l , r = 0 , len(nums) - 1
        while l < r :
            num = (nums[l] + nums[r]) / 2
            if num not in res:
                res.append(num)
            l += 1
            r -= 1
        return len(res)