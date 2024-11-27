class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array to allow skipping duplicates
        quads = []  # To store the result

        # Iterate over each number in the array as the first element of the quadruplet
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number

            # Iterate over the array as the second element of the quadruplet
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for the second number

                # Use two pointers to find the last two elements
                left, right = j + 1, len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        # Found a valid quadruplet
                        quads.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for the third and fourth numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move the pointers to continue searching
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1  # We need a larger sum, so move the left pointer to the right
                    else:
                        right -= 1  # We need a smaller sum, so move the right pointer to the left

        return quads
        