class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        memo = {}
        def backtrack(index,path):
            nonlocal res
            nonlocal memo
 
            if(index >= len(nums)):
                res = max(res,path)
                return

            if index in memo:
                res = max(res,memo[index]+path)
                return            
            
            before = res

            backtrack(index+1, path)
            backtrack(index+2, path+nums[index])
            memo[index] = res - before
           
        
        backtrack(0,0)
        return res


# [1,10,3,5,2]