class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            #mid = (r - l) // 2 + l 不會出現溢位
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
