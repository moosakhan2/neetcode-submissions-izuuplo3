class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end = 0
        cur = 0
        res = float("-inf")

        while end != len(nums):
            cur += nums[end]
            print(cur)

            res = max(res,cur)

            if cur < 0:
                cur = 0
            
            

            end+=1
           
        
        return res
        

            

        