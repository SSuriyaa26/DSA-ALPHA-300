#leetcode Q 57
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        l = 0

        while l < len(intervals):
            #add intervals less than the new intervals
            if intervals[l][1] < newInterval[0]:
                result.append(intervals[l])

            #breaking loop for intervals that occur after
            elif intervals[l][0] > newInterval[1]:
                break
            #when the new interval overlaps an interval in the list,merge logic
            else:
                if intervals[l][0] < newInterval[0]:
                    newInterval[0] = intervals[l][0]

                if intervals[l][1] > newInterval[1]:
                    newInterval[1] = intervals[l][1]


            l += 1

        result.append(newInterval)
        #adds intervals after adding new interval
        while l < len(intervals):
            result.append(intervals[l])
            l += 1

        return result