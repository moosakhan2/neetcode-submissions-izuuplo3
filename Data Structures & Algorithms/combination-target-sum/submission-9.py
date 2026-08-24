class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = []
        done = set()

        def dfs(i, total, res):
            if total == target:
                final.append(res) if tuple(res) not in done else []
                done.add(tuple(res))
                return
            
            if i == len(nums) or total > target:
                return
            
            dfs(i, total+nums[i], res+[nums[i]])
            dfs(i+1, total, res)

        
        dfs(0,0,[])

        return final


        