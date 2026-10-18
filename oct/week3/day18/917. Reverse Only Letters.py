#leetcode Q917
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s2 = ""
        while (l < len(s)):
            if (not s[l].isalnum() or s[l].isdigit()):
                s2 += s[l]
                l += 1
            else:
                while not s[r].isalnum() or s[r].isdigit():
                    r -= 1

                s2 += s[r]
                l += 1
                r -= 1
        return s2

