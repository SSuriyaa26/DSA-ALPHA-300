#leetcode Q796
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False#base case
        res = s
        res += s
        l = 0
        r = len(goal)
        while r <= len(res):
            if res[l:r] == goal:
                return True
            l += 1
            r += 1

        return False