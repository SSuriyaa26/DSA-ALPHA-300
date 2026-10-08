#leetcode Q647
'''
#Brute force method , 131/132 TLE
class Solution:
    def countSubstrings(self, s: str) -> int:
        count =0
        for i in range (len(s)):
            for j in range (i,len(s)):
                window = True #var to check if the given window is a palindrome
                l=i
                r=j
                while(l<r):#check if its palindrome
                    if s[l]!=s[r]:
                        window =False
                        break # this break got it from 130/132 to 131/132 TLE
                    l+=1
                    r-=1
                if window:
                    count+=1
        return count
This approach is very slow , O(N^3)
'''
