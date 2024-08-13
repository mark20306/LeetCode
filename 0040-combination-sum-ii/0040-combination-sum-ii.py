class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(num, path, total):
            if total > target:
                return
            elif total == target:
                ans.append(path)
                return
            for i in range(num, len(candidates)):
                if i > num and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], total + candidates[i])

        backtrack(0, [], 0)
        return ans
