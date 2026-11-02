#https://www.geeksforgeeks.org/problems/nth-pentagonal-number3721/1
class Solution:
    def getNthPentagonalNum(self, n):
        # code here
        if n == 1:
              return 1

        return self.getNthPentagonalNum(n - 1) + (3 * n - 2)