#leetcode Q1122
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result=[]
        r=0
        while r<len(arr2):
            for i in arr1:
                if i==arr2[r]:
                    result.append(i)
            r+=1
        unsorted=[]
        for i in arr1:
            if i not in arr2:
                unsorted.append(i)
        for i in range(len(unsorted)):
            for j in range(i,len(unsorted)):
                if unsorted[i]>unsorted[j]:
                    unsorted[i],unsorted[j]=unsorted[j],unsorted[i]
        result+=unsorted
        return result