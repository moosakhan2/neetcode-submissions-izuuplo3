class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       LIS = [1] * len(nums)

       for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j]+1)
        
       return max(LIS)

         
                  


            


# [1 10 10 10 10 12 3 4 5 6 7 8 9]

        

