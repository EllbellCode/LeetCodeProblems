class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Iterate from left to right
        # Say we have nums = [-2,1,-3,4,-1,2,1,-5,4]
        # The after index 0 our sum is -2
        # At index 1, we can choose to start again or add to our existing sum
        #  -2 + 1 = -1 < 1 so we should just start again
        # keep track of our max sum

        best_score = -10**4 - 1
        current_score = -10**4 - 1
        for i in range(len(nums)):

            current_num = nums[i]
            current_score += nums[i]

            if current_num > current_score:

                current_score = current_num

            if current_score > best_score:

                best_score = current_score

        return best_score 


        