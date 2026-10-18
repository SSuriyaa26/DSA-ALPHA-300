#leetcode Q58
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=-1
        while abs(r)<=len(s) and s[r]==" ":
            r-=1
        count=0
        while abs(r)<=len(s) and s[r]!=" ":
            r-=1
            count+=1
        return count
