#!/usr/bin/env python
class Solution:
    def pow(self, x, n):
        return 1 if n == 0 else pow(x, n-1) * x

solution = Solution()
print solution.pow(2.1, 2)
