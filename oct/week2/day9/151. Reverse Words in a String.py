#leetcode Q151
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")# make sentence into words
        result=""
        r=len(words)-1
        while r>=0:
            while words[r]=='' and r>0:# skip empty space in between
                r-=1
            result+= words[r].strip()
            result+=" "
            r-=1
        return result.strip()#remove whitespaces