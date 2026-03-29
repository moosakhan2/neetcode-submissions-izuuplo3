class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in mymap):
                return[mymap[diff], i]
            mymap[nums[i]] = i
        

        