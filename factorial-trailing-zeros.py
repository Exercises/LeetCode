#!/usr/bin/env python

class Solution:
    def trailingZeros(self, n):
        sum,pow5 = 0, 5
        while(n >= pow5):
            sum += n/pow5
            pow5 *= 5
        return sum

solution = Solution()
print "trailing of is 25", solution.trailingZeros(25)
print "trailing of is 100", solution.trailingZeros(100)
