class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)

        maxL = 0

        for num in m:

            if num - 1 in m:
                continue
            
            temp = 0

            while num in m:
                temp += 1
                num+=1
            
            maxL = max(temp,maxL)
        
        return maxL
            
