# leetcode Q344
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while (l < r):
            temp = s[r]# temp to swap the postions
            s[r] = s[l]
            s[l] = temp
            l += 1
            r -= 1

