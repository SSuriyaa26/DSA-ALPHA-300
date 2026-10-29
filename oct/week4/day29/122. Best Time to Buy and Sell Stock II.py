#leetcode Q122
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]-current>0:
                maxprofit+=prices[i]-current
                current = prices[i]
            if prices[i]<current:
                current=prices[i]
        return maxprofit