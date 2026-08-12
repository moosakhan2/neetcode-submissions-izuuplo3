class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        minv = prices[0]

        for i in range(1,len(prices)):
            maxprofit = max(maxprofit, prices[i]-minv)
            minv = min(minv, prices[i])
        
        return maxprofit

