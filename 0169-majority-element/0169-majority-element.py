class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        more = None
        count = 0
        for i in nums:
            if count == 0:
                more = i
                count = 1
            elif i == more:
                count += 1
            else: 
                count -= 1
        return more    