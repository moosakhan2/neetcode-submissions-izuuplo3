class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()
        
    

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            target = -nums[i]

            while l < r:
                if nums[l] + nums[r] > target:
                    r-=1
                    continue
                elif nums[l] + nums[r] < target:
                    l+=1
                    continue
                else:
                    res.add((nums[i], nums[l], nums[r]))
                l+=1
                r-=1
            
        
        return [list(t) for t in res]


            