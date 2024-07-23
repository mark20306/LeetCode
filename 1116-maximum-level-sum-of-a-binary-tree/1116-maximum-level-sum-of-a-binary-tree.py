# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        Level = 1
        ans = 0
        queue = deque([root])
        while queue:
            temp = 0
            len_root = len(queue)
            for i in range(len_root):
                node = queue.popleft()
                temp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if temp > maxSum:
                maxSum = temp
                ans = Level
            Level += 1
        return ans
        

