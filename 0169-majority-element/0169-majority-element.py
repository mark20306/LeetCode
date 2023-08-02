class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            hash_table[i]=hash_table.get(i , 0)+1
            if hash_table[i]>(len(nums))//2:                
                return i