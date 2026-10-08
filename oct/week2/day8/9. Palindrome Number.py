#leetcode Q9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        onum=x#copy of x
        num=onum%10
        onum=int (onum/10)
        while(onum!=0):#reverse number
            num*=10
            num+=onum%10
            onum = int(onum/10)
        if x==num:
            return True
        return False