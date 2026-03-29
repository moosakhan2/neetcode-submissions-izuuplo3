class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums.sort()
        freq1 = collections.defaultdict(int)

        for num in nums:
            freq1[num]+=1

        print(freq1)

        freq1 = dict(sorted(freq1.items(), key=lambda x: x[1], reverse = True))
        
        freq2 = collections.defaultdict(list)

        for key in freq1:
            freq2[freq1[key]].append(key)
        
        print(freq2)
        
        res = []
        i = 0
        
        # []

        for key in freq2:
            if (i < k):
                res += freq2[key]
                i += len(freq2[key])
        
        return res



        