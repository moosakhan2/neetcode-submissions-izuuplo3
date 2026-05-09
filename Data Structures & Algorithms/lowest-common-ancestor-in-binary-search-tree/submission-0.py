# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # USE DFS to save values in array
        res = []
        def dfs(cur, p):
            nonlocal res
            if cur == None:
                return
            if cur.val < p:
                res.append(cur)
                dfs(cur.right, p)
            elif cur.val > p:
                res.append(cur)
                dfs(cur.left, p)
            else:
                res.append(cur)
            return

        dfs(root, p.val)
        pa = res.copy()
        res = []

        dfs(root,q.val)
        qa = res.copy()

       
        # if you have 2 diff values, see the most different element
        for i in range(len(pa)):
            print(pa[i].val)
        for i in range(len(qa)):
            print(qa[i].val)
        
        length = min(len(pa), len(qa))

        for i in range(length):
            if(pa[i].val == qa[i].val):
                continue
            return pa[i-1]
        
        if(len(qa)>len(pa)):
            return(pa[i])
        return(qa[i])
        
