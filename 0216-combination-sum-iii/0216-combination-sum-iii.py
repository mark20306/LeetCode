class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(start, numSum, current):
            if len(current) == k and numSum == n:
                ans.append(current)
                return
            for i in range(start, 10):
                if numSum + i <= n:
                    backtrack(i + 1, numSum + i, current + [i])

        backtrack(1, 0, [])
        return ans
        