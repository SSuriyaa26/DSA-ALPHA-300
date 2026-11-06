#http://geeksforgeeks.org/problems/pascal-triangle0652/1

class Solution:
	def nthRowOfPascalTriangle(self, n):
	    # code here
        if n ==1:
            return [1]
        last_row= self.nthRowOfPascalTriangle(n-1)
        new_row=[1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i]+last_row[i+1])
        new_row.append(1)
        return new_row


