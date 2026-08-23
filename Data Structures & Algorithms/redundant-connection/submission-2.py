class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(node):
            if parent[node] != node:
                return(find(parent[node]))
            return parent[node]
        
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False

            if rank[ra] < rank[rb]:
                ra,rb = rb,ra
            
            parent[rb] = ra

            if rank[a] == rank[b]:
                rank[a]+=1
            
            return True
        
        for [a,b] in edges:
            if not union(a,b):
                return [a,b]
        








