#leetcode Q344
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(i):
            if i >= len(s) // 2:
                return

            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

            rev(i+1)

        rev(0)
