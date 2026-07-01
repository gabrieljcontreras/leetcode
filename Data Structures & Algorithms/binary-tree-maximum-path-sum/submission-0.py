# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        
        def dfs(node):
            if not node: 
                return 0
            
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            curr_sum = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, curr_sum)

            return node.val + max(right_gain, left_gain)
        dfs(root)

        return self.max_sum
