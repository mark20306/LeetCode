class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = 1
        for j in range(2, len(nums)):
            if nums[j] != nums[i-1]:
                i += 1
                nums[i] = nums[j]
                #print(nums)
        
        return i + 1            