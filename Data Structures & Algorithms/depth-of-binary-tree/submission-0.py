# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def dfs(cur, c):
            nonlocal max_length
            
            if cur == None:
                max_length = max(c,max_length)
                return 0
            
            return max(dfs(cur.left, c+1),dfs(cur.right, c+1))
        
        dfs(root,0)
        return max_length
        
        
        