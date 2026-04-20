class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start in reverse
        #first scan for all treasure chests and store their coordinates in queue
        # we will apply BFS

       
        def Move(i,j, target, visited, q):
            if (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and (i,j) not in visited and grid[i][j] == 2147483647):
                print(i,j)
                visited.add((i,j))
                q.append([i,j])
                grid[i][j] = target
            
           
            return


        visited = set()
        q = collections.deque()


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited.add((i,j))
                    q.append([i,j])

        
        target = 0
        while q:
            target += 1
            for j in range(len(q)):
                temp = q.popleft()
                ROW = temp[0]
                COL = temp[1]
                Move(ROW+1, COL, target, visited, q)
                Move(ROW-1, COL, target, visited, q)
                Move(ROW, COL+1, target, visited, q)
                Move(ROW, COL-1, target, visited, q)
            
        



