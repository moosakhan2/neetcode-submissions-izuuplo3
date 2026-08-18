class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        atlantic = set()
        pacific = set()

        def MOVE(i,j,ocean,prev):
            if i < 0 or i >= len(heights) or j < 0 or j>=len(heights[0]) or (i,j) in ocean or heights[i][j] < prev:
                return
            
            ocean.add((i,j))

            MOVE(i+1,j,ocean,heights[i][j])
            MOVE(i-1,j,ocean,heights[i][j])
            MOVE(i,j+1,ocean,heights[i][j])
            MOVE(i,j-1,ocean,heights[i][j])




        prev = -1    

        # Pacific Left and Atlantic RIght
        for i in range(len(heights)):
            MOVE(i,0,pacific,prev)
            MOVE(i,len(heights[0])-1, atlantic,prev)
        
        # Pacific Left Edge
        for j in range(len(heights[0])):
            MOVE(0,j,pacific,prev)
            MOVE(len(heights)-1, j, atlantic,prev)
            

        res = [list(k) for k in list(atlantic.intersection(pacific))]
        return res
        
