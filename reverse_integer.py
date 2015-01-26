class Solution:
    # @return an integer
    def reverse(self, x):
        if x >= 0:
            source = x
        else:
            source = -x
        result = 0
        while(source > 0):
            result = result * 10 + (source % 10)
            source = source / 10
        if x < 0:
            result = -result
        if(x >= 0 and result <=0 or x < 0 and result >= 0):
            result = 0
        return result
solution = Solution()
print solution.reverse(-1345)
print solution.reverse(1345)
print solution.reverse(0)
print solution.reverse(1000)
print solution.reverse(1000000003)
print solution.reverse(11000000003)
