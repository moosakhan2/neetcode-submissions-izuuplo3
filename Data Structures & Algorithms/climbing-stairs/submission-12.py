class Solution:
    def climbStairs(self, n: int) -> int:

        memo = collections.defaultdict(int)
        def backtrack(remaining):        
            if remaining in memo:
                return memo[remaining]
            if(remaining == 0):
                return 1
            
            if(remaining < 0):
                return 0 
            
            memo[remaining] += backtrack(remaining-1)+backtrack(remaining-2)

            return(memo[remaining])

            
        return(backtrack(n))
       