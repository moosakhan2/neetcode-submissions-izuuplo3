# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Left, root, right
        def recursive(cur):
            nonlocal k
  
            if cur == None:
                return



            left = recursive(cur.left)
            if left is not None:
                return left
            k-=1 
            if k == 0:
                return cur.val
            right = recursive(cur.right)
            if right is not None:
                return right
        return recursive(root)
           
        