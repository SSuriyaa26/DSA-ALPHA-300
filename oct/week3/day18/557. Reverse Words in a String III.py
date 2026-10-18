#leetcode Q557
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        result=[""]
        idx=0
        for i in words:
            r=len(i)-1
            while r>=0:
                result[idx]+=i[r]
                r-=1
            idx+=1
            result.append("")
        return " ".join(result).strip()