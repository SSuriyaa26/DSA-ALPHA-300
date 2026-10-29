#leetcode Q121
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            currentProfit = prices[i] - minPrice

            if currentProfit > maxProfit:
                maxProfit = currentProfit

            if prices[i] < minPrice:
                minPrice = prices[i]

        return maxProfit
