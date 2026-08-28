class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for course in prerequisites:
            graph[course[0]].append(course[1])
        
        # 0 for unvisited
        # 1 for visiting
        # 2 for visited
        
        res = []

        state = [0] * numCourses   # 0 = unvisited, 1 = visiting (on current path), 2 = done

        def dfs(course):
            if state[course]==1:
                return False
            
            if state[course]==2:
                return True
                
            
            state[course] = 1

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            
            res.append(course)
            state[course]=2

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
        
