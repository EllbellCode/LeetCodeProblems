class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Greedy
        # Iterate through the list
        # At each step, make the furthest jump
        # Maintain a max_reach variable

        if len(nums) == 1:
            return True

        target = len(nums) - 1
        max_reach = 0

        for i in range(len(nums)):

            if i <= max_reach:
            
                reach = i + nums[i]

                if reach > max_reach:

                    max_reach = reach

                if max_reach >= target:
                    
                    return True

        return False




                        


        

                        
            


            



            
        