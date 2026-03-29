class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minV = 1
        maxV = 1
        res = float("-inf")
      

        for i in range(len(nums)):
            num = nums[i] # 4
            temp = minV # -6
            minV = min(minV*num, maxV*num, num) # -24
            maxV = max(maxV*num, temp*num, num) # 2
            res = max(res,maxV) # 2
        return res

        
            


        
# Discuss some cases
# [1, 2, 3, 4] (all positive)

# [1, 2, -3] (negative)

# [1, 2, -3, -4] (positive) 

# [1, 2, 0, 4] (we reset current min and max to 1 after storing in global var)
# Idea is to have a min and max product
