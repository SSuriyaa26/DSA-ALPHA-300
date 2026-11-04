#leetcode 1837
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        return n % k + self.sumBase(n // k, k)