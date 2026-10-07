#geeksforgeeks
''' first attempt , TLE since the if statements take an extra O(N) times
class Solution:
    def findUnion(self, a, b):
        unique = list() # tried using a set but when converting set back to list it lost order
        l = 0
        r = 0
        while (l < len(a) or r < len(b)):
            if r >= len(b):
                if a[l] in unique:
                    l += 1
                    continue
                unique.append(a[l])
                l += 1
            elif l >= len(a):
                if b[r] in unique:
                    r += 1
                    continue
                unique.append(b[r])
                r += 1
            elif a[l] < b[r]:
                if a[l] in unique:
                    l += 1
                    continue
                unique.append(a[l])
                l += 1
            elif b[r] < a[l]:
                if b[r] in unique:
                    r += 1
                    continue
                unique.append(b[r])
                r += 1
            else:
                if b[r] in unique:
                    r += 1
                    continue
                unique.append(a[l])
                l += 1
                r += 1

        return unique
'''

# Complete Solution

class Solution:
    def findUnion(self, a, b):
        unique = list()
        l = 0
        r = 0
        while (l < len(a) or r < len(b)):
            if r >= len(b):
                if len(unique) == 0 or unique[-1] != a[l]: #The len makes sure that index isnt out of range and to check if last element in the list is not the same as current pointer element
                    unique.append(a[l])
                l += 1
            elif l >= len(a):
                if len(unique) == 0 or unique[-1] != b[r]:
                    unique.append(b[r])
                r += 1
            elif a[l] < b[r]:
                if len(unique) == 0 or unique[-1] != a[l]:
                    unique.append(a[l])
                l += 1
            elif b[r] < a[l]:
                if len(unique) == 0 or unique[-1] != b[r]:
                    unique.append(b[r])
                r += 1
            else:
                if len(unique) == 0 or unique[-1] != a[l]:
                    unique.append(a[l])
                l += 1
                r += 1

        return unique

