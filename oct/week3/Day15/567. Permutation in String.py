#leetcode Q567
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)

        if w > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(w):
            count1[ord(s1[i])-ord('a')]+=1
            count2[ord(s2[i])-ord('a')]+=1

        l = 0
        r = w - 1

        while r < len(s2):
            if count1 == count2:
                return True

            r += 1

            if r < len(s2):
                count2[ord(s2[r]) - ord('a')] += 1
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1

        return False