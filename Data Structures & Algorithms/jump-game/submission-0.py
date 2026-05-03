class Solution:
    def canJump(self, nums: List[int]) -> bool:
        need = 1
        for i in range(len(nums)-2,-1,-1):
            num = nums[i]
            if num >= need:
                need = 1
            else:
                need+=1
        
        if need == 1:
            return True
        
        return False