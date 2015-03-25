class Solution:
    def titleToNumber(self, s):
        return reduce(lambda x, y: x* 26 + y, map(lambda x : ord(x) - 64, s))

solution = Solution()
print solution.titleToNumber("A")
print solution.titleToNumber("AB")

