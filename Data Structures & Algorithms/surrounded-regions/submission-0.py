class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()

        def DFS(i,j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in visited or board[i][j] != 'O':
                return
            
            visited.add((i,j))

            DFS(i+1,j)
            DFS(i-1,j)
            DFS(i, j+1)
            DFS(i, j-1)

            return

            
            
                

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1) and board[i][j] == 'O':
                    DFS(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
        

        
