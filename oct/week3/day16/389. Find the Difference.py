#leetcode Q389
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict = {}

        for i in range(len(s)):
            dict[s[i]] = dict.get(s[i], 0) + 1
            dict[t[i]] = dict.get(t[i], 0) + 1

        dict[t[-1]] = dict.get(t[-1], 0) + 1

        for i in range(len(t)):
            if dict[t[i]] % 2 != 0:
                return t[i]
        return ""
    