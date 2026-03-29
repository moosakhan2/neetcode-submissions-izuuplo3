class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current = []

        def recursive(target, current, start_index):
            
            if target == 0:
                res.append(current.copy())
                return
            
            if target<0:
                return
            
            for i in range(start_index, len(nums)):
                current.append(nums[i])
                recursive(target-nums[i], current, i)
                current.pop()
            
            
            return
        recursive(target, current, 0)
        return res