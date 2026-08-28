class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for course in prerequisites:
            graph[course[0]].append(course[1])
        
        # 0 for unvisited
        # 1 for visiting
        # 2 for visited

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
            

            state[course]=2

            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        