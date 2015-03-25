import sys
class Solution:
    def generate(self, numRows):
        pascal = []
        for row in range(0, numRows):
            cur_list = [ 1 if i == 0 or i == row else pascal[row-1][i] + pascal[row-1][i-1] for i in range(0, row +1)]    
            pascal.append(cur_list)
        return pascal

solution = Solution()
numRows = int(sys.argv[1])
print "numRows : ", numRows 
print solution.generate(numRows)
