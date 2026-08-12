class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
    
        def alphanumeric(c):
            if '0' <= c <= '9' or 0<= ord(c)-ord('a') <= 26:
                return True
            return False


        while l < r:
            if not alphanumeric(s[l].lower()):
                l+=1
                continue
            elif not alphanumeric(s[r].lower()):
                r-=1
                continue
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True

        