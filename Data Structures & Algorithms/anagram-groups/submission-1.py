class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        def convertintoAnagram(word):
            res = [0] * 26
            
            for char in word:
                res[ord(char) - ord('a')] +=1
            
            return tuple(res)
        
        for word in strs:
            hashmap[convertintoAnagram(word)].append(word)
        
        res = []
        for key in hashmap:
            res.append(hashmap[key])

        return res

        