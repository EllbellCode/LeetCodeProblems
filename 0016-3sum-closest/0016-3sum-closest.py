class Solution(object):
    def threeSumClosest(self, nums, target):
        # Sort the array to manage duplicates and use two-pointer technique
        nums.sort()
        closest = 100000
    
        for i in range(len(nums) - 2):
        
            # Two-pointer search
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = current_sum - target

                if diff == 0:
                    return target
            
                if abs(diff) < closest:
                    closest = abs(diff)
                    closest_sum = current_sum

                if diff < 0:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
       