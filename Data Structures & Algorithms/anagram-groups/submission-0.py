class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = collections.defaultdict(list)
        
        for string in strs:
            single_freq = [0] * 26
            for char in string:
                single_freq[ord(char) - ord('a')] += 1
            
            freq[tuple(single_freq)].append(string)
        
        return list(freq.values())