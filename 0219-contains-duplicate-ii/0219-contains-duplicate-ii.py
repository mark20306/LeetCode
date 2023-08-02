class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash={}
        for i , num in enumerate(nums):
            if num in hash :  
                if i - hash[num] <= k:              
                    return True
            
            hash[num] = i
        return False        
