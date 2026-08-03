class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff],i]
            
            hashmap[num] = i
        
        