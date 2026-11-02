#leetcode 172
class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n==1 or n==0:
                return 1
            else:
                return n*fact(n-1)
        num=fact(n)
        count=0
        while(num%10==0):
                num//=10
                count+=1
        return count