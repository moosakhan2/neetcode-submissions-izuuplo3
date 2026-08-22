class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for course in prerequisites:
            graph[course[0]].append(course[1])

        # 0 for not visited
        # 1 for visiting
        # 2 for visited

        state = [0] * numCourses

        courseList = []
        inCourseList = set()
        
        def check(node):
            nonlocal courseList

            if state[node] == 2:
                return True
            
            if state[node] == 1:
                return False
            
            state[node] = 1
            
            for course in graph[node]:
                if not check(course):
                    return False

            state[node] = 2
            if node not in inCourseList:
                courseList.append(node)
                inCourseList.add(node)
            return True 
        
        if not all(check(c) for c in range(numCourses)):
            return []
        
        return(courseList)

        



        