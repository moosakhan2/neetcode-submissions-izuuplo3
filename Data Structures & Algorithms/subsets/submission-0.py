class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        visit = set()

        def dfs(i, res):
            if i == len(nums):
                final.append(res)
                return
            

            dfs(i+1, res + [nums[i]]) 
            dfs(i+1, res)
        
        dfs(0,[])

        return final
            

        