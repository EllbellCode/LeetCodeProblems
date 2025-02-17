class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Given n is the length of nums then time complexity here is O(n**2)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                        return [i,j]
        """
        left, right = 0, len(nums)-1
        nums_sort = sorted(nums)
        while left < right:
            left_num = nums_sort[left]
            right_num = nums_sort[right]
            if left_num + right_num == target:
                left_index = nums.index(left_num)
                right_index = nums.index(right_num)
                if left_num == right_num:
                    nums.remove(left_num)
                    right_index = nums.index(right_num) + 1
                return [left_index, right_index]
            elif left_num + right_num < target:
                left += 1
            elif left_num + right_num > target:
                right -= 1




        