class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        minValue = float("inf")

        while(l<=r):
            if(nums[l]<nums[r]):
                minValue = min(minValue,nums[l])
                break
            mid = (l+r) // 2
            minValue = min(minValue,nums[mid])

            if nums[mid] >= nums[l]:

                l = mid + 1
            
            else:
                r = mid -1
        return minValue
            
            
