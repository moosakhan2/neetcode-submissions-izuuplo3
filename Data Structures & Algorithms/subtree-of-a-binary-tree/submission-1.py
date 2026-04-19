# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def match(root1,root2):
            if(root1 == None and root2 == None):
                return True
            
            if((root1 is not None and root2 is None) or (root1 is None and root2 is not None) ):
                return False
            
            if(root1.val != root2.val):
                return False
            
            res = match(root1.left, root2.left) and match(root1.right, root2.right)

            return res
        
                
        flag = False
        def goover(root):
            nonlocal flag

            if(root == None):
                return
            
            if match(root,subRoot):
                flag = True
            print(flag)
           
            goover(root.left)
            goover(root.right)

            return
        
        goover(root)
        return flag
