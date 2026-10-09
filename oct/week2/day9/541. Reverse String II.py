#leetcode Q541
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        letters = list(s)
        for i in range(0, len(letters), 2 * k):
            start = i
            end = i + k - 1
            if end>=len(letters):#case where i+k-1 is greater than n index out of range,
                end=len(letters)-1
            while start < end:
                letters[start], letters[end] = letters[end], letters[start]
                start += 1
                end -= 1
        return "".join(letters)


