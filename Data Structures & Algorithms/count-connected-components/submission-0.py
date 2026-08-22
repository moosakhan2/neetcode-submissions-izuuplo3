class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        state = [False] * n
        def check(node,parent):
            if state[node]:
                return
            
            state[node] = True

            for curr in graph[node]:
                if curr == parent:
                    continue
                check(curr, node)
            
            return
        
        res = 0
        for i in range(n):
            if not state[i]:
                res+=1
                check(i,-1)

        return res

            

