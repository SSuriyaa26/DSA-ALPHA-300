#leetcode Q1207

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count={}
        for i in range(len(arr)):
            count[arr[i]]=count.get(arr[i],0)+1
        unique=set()
        li=list(count.values())#list with all the vals and checking duplicates from that

        #more optimal soln is return len(count.values())==len(set(count.values())
        for i in range(len(li)):
            if li[i] in  unique:
                return False
            unique.add(li[i])
        return True