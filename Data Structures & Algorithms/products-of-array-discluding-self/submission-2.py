class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        r = [1]

        product = nums[0]

        for i in range(1, len(nums)):
            l.append(product)
            product*=nums[i]
        
        product = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            r.append(product)
            product*=nums[i]

        print(l,r)
        

        res = []

        for i in range(len(l)):
            res.append(l[i] * r[len(l)-i-1])
        
        return res
