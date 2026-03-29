class Solution:
    def climbStairs(self, n: int) -> int:

        memo = collections.defaultdict(int)
        def backtrack(steps, remaining):        
            if remaining in memo:
                return memo[remaining]
            if(steps == n):
                return 1
            
            if(steps > n):
                return 0 
            
            memo[remaining] += backtrack(steps+1,remaining-1)+backtrack(steps+2, remaining-2)

            return(memo[remaining])

            
        return(backtrack(0, n))
       