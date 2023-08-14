class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        print(n)
        res = []
        for i in range(len(n)):
            if i > 0 and n[i] == n[i - 1]:
                continue
            l , r = i+1 , len(n) - 1
            while l < r:
                if n[i] + n[l] + n[r] > 0:
                    r -= 1
                elif n[i] + n[l] + n[r] < 0:
                    l += 1
                else:
                    res.append([n[i] , n[l] , n[r]])
                    r -= 1
                    l += 1
                    while n[l] == n[l-1] and l < r:
                        l += 1
        return res                