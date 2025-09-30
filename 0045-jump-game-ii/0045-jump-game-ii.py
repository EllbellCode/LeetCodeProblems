class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jumps = 0 
        current_reach = 0 #furthest we can reach with current number of jumps
        furthest = 0 

        # Stop at second to last element instead of last
        # Guaranteed to get to last element from here or the actul jump has already been counted
        for i in range(len(nums)-1):

            new = i + nums[i]
            furthest = max(furthest, new)

            if furthest >= len(nums)-1:
                return jumps + 1

            if i == current_reach:

                jumps += 1
                current_reach = furthest

        return jumps





        