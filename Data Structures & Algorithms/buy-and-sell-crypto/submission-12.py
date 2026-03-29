class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        minValue = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit, prices[i]-minValue)
            minValue = min(minValue, prices[i])
        
        if profit > 0:
            return profit

        return 0
        
            

        