#leetcode Q 1051
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected=heights[:]#copy , direct copy doesnt work
        #sort expected
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                if expected[i]>expected[j]:
                    expected[i],expected[j]=expected[j],expected[i]
        l=0
        result=0
        #compare expected and heights , if misplaced add count
        while(l<len(expected)):
            if heights[l]!=expected[l]:
                result+=1
            l+=1
        return result