class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        travel = [1, 0, 0, 0]

        visited = set()
        res = []
        i = 0
        j = 0
        
        visited.add((0,0))
        res.append(matrix[0][0])
        


        def move(i, j):
            if (i,j) in visited:
                for k in range(len(travel)):
                    if travel[k]:
                        travel[k] = 0
                        travel[(k+1) % 4] = 1
                        return True
            else:
                visited.add((i,j))
                res.append(matrix[i][j])
                return False



        while(len(visited) != (len(matrix)*len(matrix[0]))):
            if travel[0]:
                j += 1
                if j == len(matrix[0]):
                    j-=1
                    travel[0] = 0
                    travel [1] = 1
                else:
                    if move(i, j):
                        j-=1  
                          
                
            elif travel[1]:
                 
                i += 1
                if i == len(matrix):
                    i-=1
                    travel[1] = 0
                    travel[2] = 1
                else:
                    if move(i, j):
                        i-=1 
                        
            
            elif travel[2]:
                j -= 1
                if j == -1:
                    j = 0
                    travel[2] = 0
                    travel[3] = 1
                else:
                    if move(i, j):
                        j+=1
                            

            elif travel[3]:
                i -= 1
                if i == -1:
                    i = 0
                    travel[3] = 0
                    travel[0] = 1
                else:
                    if move(i,j):
                        i+=1
                        
            
            
            
        return res


