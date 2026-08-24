class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()

        def dfs(i, res):
            if i >= len(nums):
                final.append(res)
                return
            

            dfs(i+1, res+[nums[i]])

            nxt = i+1
            while nxt < len(nums) and nums[nxt] == nums[i]:
                nxt+=1
            
            dfs(nxt, res)


        dfs(0,[])
        return final

        