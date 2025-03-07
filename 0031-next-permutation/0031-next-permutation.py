class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #default pivot value out of range contraints
        pivot = -1

        #find pivot value
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]: 
                pivot = i
                break

        #if we still have default pivot value
        #then the array is in largest lexicographic order
        # so we reverse 
        if pivot == -1:
            nums.reverse()
            return nums
        
        
        # set default value to pivot if there is no element less than pivot
        swap_index = pivot

        # find pivot value
        for i in range(len(nums) - 1, pivot, -1):  
            if nums[i] > nums[pivot]: 
                swap_index = i
                break
            
        #swap pivot and swap around
        nums[pivot], nums[swap_index] = nums[swap_index], nums[pivot]

        #two pointers to reverse right side of pivot
        left, right = pivot+1, len(nums)-1
        while left < right:

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums