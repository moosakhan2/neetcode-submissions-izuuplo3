class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for [a,b] in prerequisites:
            graph[a].append(b)
        
        # 0 for unvisited
        # 1 for visiting
        # 2 for visited

        state = [0] * numCourses
        res = []

        def takeCourse(node):
            nonlocal res
            if state[node] == 2:
                return True
            
            if state[node] == 1:
                return False
            
            state[node] = 1
            
            for curr in graph[node]:
                if not takeCourse(curr):
                    return False
            
            state[node] = 2
            res.append(node)

            return True
        
        for i in range(numCourses):
            if not takeCourse(i):
                return []
        return res
        
