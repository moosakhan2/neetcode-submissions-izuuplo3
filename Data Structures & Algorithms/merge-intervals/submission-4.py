class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if res == []:
                res.append(interval)
                continue

            if(interval[0]==res[-1][0]):
                res[-1][1] = max(interval[1], res[-1][1])
            
            elif(interval[0] <= res[-1][1]):
                res[-1][1] = max(interval[1], res[-1][1])
                res[-1][0] = min(interval[0], res[-1][0])
        
                
            else:
                res.append(interval)
        return res


                    