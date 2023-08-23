class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in nums1:
            l , r = 0 , len(nums2) - 1
            while l <= r:
                mid = (r - l) // 2 + l
                if i == nums2[mid]:
                    return i
                elif i < nums2[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1    