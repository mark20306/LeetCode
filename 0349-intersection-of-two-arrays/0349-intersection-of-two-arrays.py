class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()

        for i in nums1:
            l , r = 0 , len(nums2) - 1
            while l <= r:
                mid = (r - l) // 2 + l
                if nums2[mid] == i and i not in res:
                    res.append(i)
                    
                elif nums2[mid] > i:
                    r = mid - 1
                else:
                    l = mid + 1
        return res
