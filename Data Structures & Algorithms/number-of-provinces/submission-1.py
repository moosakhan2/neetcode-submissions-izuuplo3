class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        N = len(isConnected)
        parent = [i for i in range(N)]
        rank = [0] * N

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node]) 

            return parent[node]

        provinces = N

        def union(a, b):
            nonlocal provinces
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            
            provinces -= 1
            if rank[ra] < rank[rb]:
                rb, ra = ra, rb

            parent[rb] = ra

            if rank[ra] == rank[rb]:
                rank[ra] += 1

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    union(i, j)

        return provinces