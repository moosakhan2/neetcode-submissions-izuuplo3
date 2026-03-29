class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        check = {}
        # [-4, -1, -1, 0, 1, 2]

        for i in range(len(nums)):
            if(i > len(nums)-3):
                continue
            
            start = i+1
            end = len(nums)-1


            target = -(nums[i]) #4
            print(target)
            # apply 2 sum
            freq = {}
            for j in range(start,end+1):
              
                diff = target - nums[j]
              
                if(diff in freq):
                    temp = [diff,nums[j],-target]
                    temp.sort()
                    if(tuple(temp)) not in check:
                        res.append(temp)
                        check[tuple(temp)] = True
                        

                        
      
                freq[nums[j]] = j
        
        return res

        