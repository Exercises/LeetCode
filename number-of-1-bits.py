#!/usr/bin/env python
class Solution:
    def hammingWeight(self, n):
        weight = 0
        nn = -n if n < 0 else n
        while(nn != 0):
            weight +=  nn % 2
            nn = nn / 2
        return weight
a = Solution()
print a.hammingWeight(7)
print a.hammingWeight(-7)
a.hammingWeight(7)
