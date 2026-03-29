# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        def recursive(current: Optional[TreeNode]):
            if(current is None):
                return
            
            current.left, current.right = current.right, current.left
            recursive(current.left) 
            recursive(current.right)

            return
        recursive(current)
        return current

            