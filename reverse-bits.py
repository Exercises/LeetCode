#!/usr/bin/env python

class Solution:
    def reverseBits(self, n):
        i, l = 0, [0 for i in range(0, 32)]
        while n > 0:
            l[i] = n %2
            n = n / 2
            i += 1
        return reduce(lambda x, y: x * 2 + y, l) 

solution = Solution()
print solution.reverseBits(43261596)
