class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        startProfit = prices[0]
        endProfit = []
        for i in range(1, len(prices)):
            if i == 1:
                currentProfit = startProfit
            if prices[i] > currentProfit:
                newProfit = prices[i] - currentProfit
                
                endProfit.append(newProfit)
            currentProfit = prices[i]
            i += 1
        return sum(endProfit)