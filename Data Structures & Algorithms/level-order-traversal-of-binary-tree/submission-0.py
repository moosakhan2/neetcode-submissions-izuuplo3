# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        q = collections.deque()
        if(root):
            q.append(root)
        else:
            return []

        while q:
            temp = []
            length = len(q)
        
            for i in range(length):
                node = q.popleft()
                temp.append(node.val)
      
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)

            res.append(temp)
        
    
        return res
          
        