class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        first, last = 0, len(nums) - 1


        while first <= last:
            if nums[first] == val:
               #We do not need to check if last is val
               #As the while loop will recheck first on the next pass
                nums[first], nums[last] = nums[last], nums[first]
                last -= 1
            else:
                first += 1 

        return first
        