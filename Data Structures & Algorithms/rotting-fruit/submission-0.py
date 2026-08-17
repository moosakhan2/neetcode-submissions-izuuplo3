class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        hasFresh = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    hasFresh = True
        
        if not q:
            if hasFresh:
                return -1
            else:
                return 0
        
        def MOVE(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return False
            
            grid[i][j] = 2
            q.append([i,j])
            
            

        time = -1
        while q:
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                x,y = curr[0], curr[1]
                MOVE(x+1,y)
                MOVE(x-1,y)
                MOVE(x,y+1)
                MOVE(x,y-1)
            time +=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return time

