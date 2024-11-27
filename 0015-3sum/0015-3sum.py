class Solution(object):
    def threeSum(self, nums):

        nums.sort()
        triples = []

        # -2 here to account for j and k values
        for i in range(len(nums)-2):

            #Skip duplicate values as nums is now sorted
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #Initialise 2 pointers
            left, right = i+1, len(nums)-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
            
                if current_sum == 0:
                    triples.append([nums[i], nums[left], nums[right]])
                    # Move pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return triples

        