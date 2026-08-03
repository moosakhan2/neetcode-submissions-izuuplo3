class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ntof = collections.defaultdict(int)
        fton = collections.defaultdict(list)

        for num in nums:
            ntof[num] += 1
        
        for key in ntof:
            fton[ntof[key]].append(key)
        

        fton = dict(sorted(fton.items(), reverse = True))
        res = []

        for key in fton:
            if k == 0:
                return res
            
            res.extend(fton[key])
            k-=len(fton[key])
            
        return res

        
        
