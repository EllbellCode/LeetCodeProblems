class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):  # Traverse backwards
            if nums[i] < nums[i + 1]:  # Find the first decreasing element
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return nums
        
        swap_index = pivot
        for i in range(len(nums) - 1, pivot, -1):  # Traverse from the end
            if nums[i] > nums[pivot]:  # Find the smallest larger element
                swap_index = i
                break
            
        nums[pivot], nums[swap_index] = nums[swap_index], nums[pivot]

        left, right = pivot+1, len(nums)-1

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums