#!/usr/bin/env python
class Solution:
    def sqrt(self, x):
        low, high = 0, x
        if x == 1:
            return 1
        while low <= high:
            middle = (low + high) / 2
            if middle * middle > x:
                high = middle -1
            elif middle * middle < x:
                low = middle + 1
            else:
                break
        return low -1 if low > high else  middle

solution = Solution()
print 100, solution.sqrt(100)
print 10, solution.sqrt(10)
print 0, solution.sqrt(0)
print 1, solution.sqrt(1)
print 2, solution.sqrt(2)
print 6, solution.sqrt(6)
