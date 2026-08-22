class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        # 0: 1
        # 1: 0, 2, 3, 4
        # 2: 1, 3
        # 3: 1, 2, 4
        # 4: 1


        # 0 for not visited
        # 1 for visiting
        # 2 for visited

     
        visited = set()

        def visit(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            
            for curr in graph[node]:
                if curr == parent:
                    continue
                if not visit(curr, node):
                    return False

            return True
        
        return visit(0,-1) and len(visited) == n