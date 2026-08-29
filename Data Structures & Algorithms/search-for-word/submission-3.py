class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        q = deque()

        temp = board.copy()

        def dfs(pointer, i, j):
            if pointer == len(word):
                return True

            if i >= len(board) or i < 0 or j >= len(board[i]) or j < 0 or board[i][j] != word[pointer] or board[i][j] == "#":
                return False
            
         
            board[i][j] = "#"

            found = dfs(pointer+1, i+1, j) or dfs(pointer+1, i-1, j) or dfs(pointer+1, i, j+1) or dfs(pointer+1, i, j-1)
            board[i][j] = word[pointer] 
            return found
        

        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(0, i, j):
                    return True

        return False




        