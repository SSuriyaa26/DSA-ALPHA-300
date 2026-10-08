#leetcode Q125
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r= len(s)-1
        for i in s:
            #while loop to skip the non alpha numeric vals and r>=0 so that it doesnt loop back
            while r>=0 and not s[r].isalnum():
                r-=1
            if not i.isalnum():
                continue

            if i.lower() != s[r].lower():
                return False
            r-=1
        return True

'''
#works but not the most effective version

class Solution:
    def isPalindrome(self, s: str) -> bool:
        r= len(s)-1
        l=0
        while(l<r):
            while l<r and not s[r].isalnum():
                r-=1
            while l<r and not s[l].isalnum():
                l+=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True