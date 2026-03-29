class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        
        freq = {str(i): True for i in range(1, 27)}
        memo = {}

        def backtrack(i):
            if i == len(s):
                return 1
            
            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0
            

            res = backtrack(i + 1)
            
            if i + 1 < len(s) and s[i:i+2] in freq:
                res += backtrack(i + 2)

            memo[i] = res
            return res
        
        return backtrack(0)