#leetcode Q709
class Solution:
    def toLowerCase(self, s: str) -> str:
        #return s.lower()
        result=""
        for char in s:
            if ord('A')<=ord(char)<=ord('Z'):
                result+=  chr(ord(char)+32)
            else:
                result+=char
        return result