#leetcode 1431
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max1=max(candies)# find max in the given arr
        res=[]
        for i in candies:
            if max1>i+extraCandies:#check condition
                res.append(False)
            else:
                res.append(True)
        return res