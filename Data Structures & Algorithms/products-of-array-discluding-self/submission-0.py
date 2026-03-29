class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = []
        back = []

        val = 1

        for i in range(len(nums)):
            if i == 0:
                val = nums[i]
                front.append(1)
                continue
        
        
            front.append(val)
            val*=nums[i]
            
        val = 1
        for i in range(len(nums)-1, -1, -1):
            if (i == len(nums)-1):
                val = nums[i]
                back.append(1)
                continue
            num = nums[i]
            back.append(val)
            val*=num
        
        
        res = []
        print(front)
        print(back)
        for i in range(len(nums)):
            res.append(front[i]*back[len(nums)-i-1])
        
        return res
        