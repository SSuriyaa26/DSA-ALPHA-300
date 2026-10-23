#leetcode Q1475
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = []
        stack = []
        for i in range(len(prices)):
            res.append(prices[i])

        for i in range(len(prices)):
            while len(stack) > 0 and prices[stack[-1]] >= prices[i]:
                top = stack.pop()
                res[top] -= prices[i]

            stack.append(i)

        return res