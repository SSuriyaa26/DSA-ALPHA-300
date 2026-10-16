#leetcode 2351
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = {}
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1

            if count[s[i]]==2:
                return s[i]
        return ""