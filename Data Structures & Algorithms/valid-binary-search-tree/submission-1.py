# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, lo, high):
            if curr == None:
                return True
            if not (lo<curr.val<high):
                return False
            
            return dfs(curr.left, lo, curr.val) and dfs(curr.right, curr.val, high)
        
        return dfs(root, float("-inf"), float("inf"))
            
            
            
        