class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        visit = set()

        def dfs(path, used):
            if len(path) == len(nums):
                final.append(path.copy())
                return
            
            for x in nums:
                if x in used:
                    continue
                used.add(x)
                path.append(x)
                dfs(path,used)
                path.pop()
                used.remove(x)
        
        dfs([],used=set())
        return final
            
            