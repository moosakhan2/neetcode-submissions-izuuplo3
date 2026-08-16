class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i,j])
        
        if not queue:
            return
        
        counter = 1


        def MOVE(x,y):
            nonlocal counter
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or not( grid[x][y] == (2**31)-1):
                return

            queue.append([x,y])
            grid[x][y] = counter

        while queue:
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                x,y = curr[0],curr[1]
                MOVE(x+1,y)
                MOVE(x-1,y)
                MOVE(x,y+1)
                MOVE(x,y-1)
            counter += 1
        

            



        