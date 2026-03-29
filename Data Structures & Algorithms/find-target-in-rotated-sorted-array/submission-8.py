class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # [3,4,5,6,1,2]
        # [4,5,6,7,0,1,2]

        l = 0
        r = len(nums)-1
       

        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            elif nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            
        
        return -1
