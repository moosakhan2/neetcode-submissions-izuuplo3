class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = collections.defaultdict(list)


        for course in prerequisites:
            want,need = course[0],course[1]

            courseMap[want].append(need)
        
        state = [2] * numCourses

        # 0 Visited
        # 1 (in our current path i.e cycle)
        # 2 (not visited)

        def checkGraph(node):
            if state[node] == 0:
                return True
            
            if state[node] == 1:
                return False
            
            state[node] = 1
            for course in courseMap[node]:
                if not checkGraph(course):
                    return False
            state[node] = 0
            return True

        return all(checkGraph(c) for c in range(numCourses))





        