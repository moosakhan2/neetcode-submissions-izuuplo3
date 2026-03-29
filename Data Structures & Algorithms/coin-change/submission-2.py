class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res = 0
        if(amount == 0):
            return 0
        
        memo = {}

        def dfs(total, i, count):

            nonlocal res

            if(res !=0 and count > res):
                return

            if(total == amount):
                if(res == 0):
                    res = count
                else:
                    print(res)
                    res = min(count,res)
                return

            if(i==len(coins) or total > amount):
                return

           
            dfs(total, i+1, count)
            dfs(total+coins[i], i, count+1)
            dfs(total+coins[i],i+1, count+1)
                
            

        dfs(0,0,0)
            
        if(res == 0):
            return -1
        return res

        