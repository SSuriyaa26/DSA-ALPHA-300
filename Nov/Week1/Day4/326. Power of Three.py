#leetcode 326
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)

#eval: 20 ms , 18.98mb

#iteration
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1

#eval:29ms ,19.19 mb


