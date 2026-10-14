#leetcode Q438
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        w = len(p)

        if w > len(s):
            return []

        chars = [0] * 26

        for i in range(w):
            chars[ord(p[i]) - ord('a')] -= 1
            chars[ord(s[i]) - ord('a')] += 1

        res = []

        if all(x == 0 for x in chars):
            res.append(0)

        l = 0
        r = w

        while r < len(s):
            chars[ord(s[l]) - ord('a')] -= 1
            chars[ord(s[r]) - ord('a')] += 1

            if all(x == 0 for x in chars):
                res.append(l + 1)

            l += 1
            r += 1

        return res