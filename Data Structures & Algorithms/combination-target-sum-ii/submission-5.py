class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        duplicate = set()
        candidates.sort()



        def dfs(i, total, res): 
            if total == target:
                res.sort()
                if tuple(res) not in duplicate:
                    duplicate.add(tuple(res))
                    final.append(res)
                return
            
            if i == len(candidates) or total > target:
                return
            

            dfs(i+1, total+candidates[i], res+[candidates[i]])
            nxt = i + 1
            while nxt < len(candidates) and candidates[nxt] == candidates[i]:
                nxt += 1
            dfs(nxt, total, res)

        
        dfs(0,0,[])
        return final




        