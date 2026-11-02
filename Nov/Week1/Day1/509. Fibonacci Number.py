#leetcode 509
class Solution:
    def fib(self, n: int) -> int:
        if n==0:#base cases
            return 0
        if n ==1 :
            return 1
        else:#recursion
            return self.fib(n-1)+self.fib(n-2)
