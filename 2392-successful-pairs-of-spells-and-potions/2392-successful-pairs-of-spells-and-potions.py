class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []

        for i in spells:
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if i * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(len(potions) - left)  

        return ans  
            
        