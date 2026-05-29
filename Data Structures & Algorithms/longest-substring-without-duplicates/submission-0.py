import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = collections.defaultdict(int)
        start = 0
        end = 0
        res = 0

        while end < len(s):
            char = s[end]
 

            if freq[char] == 0:
                freq[char]+=1
               
            else:
                while(freq[char] > 0):
                    remove = s[start]
                    freq[remove]-=1
                    start+=1
                freq[char] = 1
            res = max(res, (end-start+1))
            end+=1


        return res
            

                    
        
        