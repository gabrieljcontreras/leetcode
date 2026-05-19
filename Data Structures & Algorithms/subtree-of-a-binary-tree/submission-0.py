# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q): #helper function to check if they are the same
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            else: 
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not subRoot and not root:  #if end at same time, they are equal
            return True 
        
        if not root or not subRoot: #else they are not
            return False
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #keep searching
        