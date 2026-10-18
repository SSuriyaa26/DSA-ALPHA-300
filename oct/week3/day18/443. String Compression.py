#leetcode 443
class Solution:
    def compress(self, chars: list[str]) -> int:
        l = 0
        r = 0
        count = 0
        res = ""
        while r < len(chars):
            if chars[l] == chars[r]:
                r += 1
                count += 1
            else:
                res += chars[l]
                if count > 1:
                    res += str(count)
                l = r
                count = 0
        res += chars[l]
        if count > 1:
            res += str(count)
        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)



