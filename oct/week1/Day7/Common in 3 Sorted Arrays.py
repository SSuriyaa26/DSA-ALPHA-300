#geeksforgeeks
'''
class Solution:
    def commonElements(self, a, b, c):
        result =[]
        for i in a:
            if i in b and i in c: # simple brute solution , check if a given element is in a is also in b and c , add into result
                if len(result) == 0 or result[-1] != i: #remove duplicate
                    result.append(i)
        return result
'''
#using the idea learned in union of 2 sorted:
class Solution:
    def commonElements(self, a, b, c):
        i = 0
        j = 0
        k = 0
        result = []

        while i < len(a) and j < len(b) and k < len(c):# we use and here , not or since its common element once an arry ends there would be no more common elements

            if a[i] == b[j] and b[j] == c[k]:
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])

                i += 1
                j += 1
                k += 1

            elif a[i] <= b[j] and a[i] <= c[k]:
                i += 1

            elif b[j] <= a[i] and b[j] <= c[k]:
                j += 1

            else:
                k += 1

        return result