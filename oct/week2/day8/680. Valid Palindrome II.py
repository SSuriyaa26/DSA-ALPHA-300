# leetcode Q680
'''
First attempt , passed 470 /477 test case

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r= len(s)-1
        count = 0
        while(l<r):
            if(s[l]!=s[r]):
                if s[l+1]==s[r]:
                    l+=1
                    count+=1
                elif s[r-1]==s[l]:
                    r-=1
                    count+=1
                else:
                    return False
            if count>1:# if more than 1 is removed then not valid.
                return False
            l+=1
            r-=1
        return True

The issue with the failing test case are if l and r both are valid options in regards to the skipping but only 1 makes a palindrome

'''
# so in the solution the check is made on both right and left sides and returns true or false

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(l, r):
            while (l < r):
                if (s[l] != s[r]):
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1

        while (l < r):
            #count var is removed since we return when the if statement is called
            if s[l] != s[r]:
                return check(l + 1, r) or check(l, r - 1)
            l += 1
            r -= 1
        return True

