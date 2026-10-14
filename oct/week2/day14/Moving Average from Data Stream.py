#GFG , im unsure if this was the right question since it seems very easy , the leetcode version was paid
#https://www.geeksforgeeks.org/problems/average4856/1
class Solution:
    def prefixAvg(self, arr):
        # code here
        res=[]
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
            res.append(int(sum/(i+1)))
        return res