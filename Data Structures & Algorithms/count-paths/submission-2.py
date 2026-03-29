class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n] * m
        
        res = 0
        def dfs(i,j):
            nonlocal res
            if not (i < m and j < n):
                return

            if(i == m-1 and j == n - 1):
                res += 1
                return
            
            dfs(i+1,j)
            dfs(i,j+1)
            
        dfs(0,0)
        return res

        