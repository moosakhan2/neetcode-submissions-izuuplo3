class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        area = 0

        def visit(i,j):
            nonlocal area
            # if basecase:
            # return counter
            if i < 0 or i >= len(grid) or j < 0 or j >=len(grid[0]) or (i,j) in visited or not grid[i][j]:
                return

            visited.add((i,j))
            area+=1
            visit(i+1,j)
            visit(i-1,j)
            visit(i,j+1)
            visit(i,j-1)



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in visited:
                    visit(i,j)
                    res = max(res, area)
                    area = 0

        return res