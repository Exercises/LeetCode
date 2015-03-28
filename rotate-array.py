class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k = k % len(nums)
        xnums = nums[-k:] + nums[0 : len(nums)-k]
        for i in range(len(nums)):
            nums[i] = xnums[i]
