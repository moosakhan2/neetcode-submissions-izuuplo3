class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0 for i in range(26)]

        for char in s:
            check[ord(char)-ord('a')] += 1
        
        for char in t:
            check[ord(char)-ord('a')] -= 1
        
        return check == [0 for i in range(26)]
        