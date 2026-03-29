class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        res = []

        for i in range(len(s)):
            char = s[i]
            if(char in mymap and res and res[-1] == mymap[char]):
                res.pop()
            else:
                res.append(char)
        
        return(res==[])
        