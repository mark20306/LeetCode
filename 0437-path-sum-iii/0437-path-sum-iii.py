# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, curr):
            if not root:
                return 0
            curr += root.val
            ans = prefixSums.get(curr - targetSum, 0)
            prefixSums[curr] = prefixSums.get(curr, 0) + 1
            ans += dfs(root.left, curr)
            ans += dfs(root.right, curr)
            prefixSums[curr] -= 1
            return ans

        prefixSums = {0: 1}
        return dfs(root, 0)
            