class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_rev = list(nums)
        nums_rev.reverse()

        if target in nums:

            return [nums.index(target), len(nums) - nums_rev.index(target) - 1]

        else:

            return [-1, -1]

        
        