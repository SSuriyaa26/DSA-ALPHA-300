#leetcode Q2000
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l=0
        r=0
        while r<len(word):
            if word[r]==ch:
                break
            r+=1
        letters=list(word)
        if r==len(word):
         return word
        while(l<r):
            temp = letters[l]
            letters[l] = letters[r]
            letters[r]=temp
            l+=1
            r-=1
        return "".join(letters)
