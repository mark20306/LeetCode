class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1 , hash2 = set(nums1) , set(nums2)        
        res1 = hash1 - hash2
        res2 = hash2 - hash1
        
        
        return res1,res2

        
