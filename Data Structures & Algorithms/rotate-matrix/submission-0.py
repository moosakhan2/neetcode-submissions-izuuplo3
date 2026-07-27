class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Row Swap (Except middle)
        for i in range(len(matrix)//2):
            temp = matrix[i]
            matrix[i] = matrix[len(matrix)-1-i]
            matrix[len(matrix)-1-i] = temp
        
        # Diagnal triangle thingy swap
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i<j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        
        