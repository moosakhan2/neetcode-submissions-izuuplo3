class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,prev, visited):
            if (i,j) in visited or i >= len(heights) or i < 0 or j >= len(heights[0]) or j < 0 or prev > heights[i][j]:
                return
            
            visited.add((i,j))
            dfs(i+1, j, heights[i][j], visited)
            dfs(i-1, j, heights[i][j], visited)
            dfs(i, j+1, heights[i][j], visited)
            dfs(i, j-1, heights[i][j], visited)

            return

        
        pacific = set()
        atlantic = set()

        # Pacific Left
        for i in range(len(heights)):
            dfs(i,0,-1, pacific)
        
        # Pacific Up
        for j in range(len(heights[0])):
            dfs(0,j,-1, pacific)
        

        # Atlantic Right
        for i in range(len(heights)):
            dfs(i, len(heights[0])-1, -1, atlantic)
        
        # Atlantic Down
        for j in range(len(heights[0])):
            dfs(len(heights)-1, j, -1, atlantic)
        

        return [list(item) for item in atlantic.intersection(pacific)]
        


            
                
                
                
        