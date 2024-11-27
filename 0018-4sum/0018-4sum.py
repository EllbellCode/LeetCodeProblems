class Solution(object):
    def fourSum(self, nums, target):
        
        nums.sort()
        quads = []

        for i in range(len(nums)-3):
            
            for j in range(len(nums)-2-i):

                left, right = i+j+1, len(nums)-1
                while left < right:
                    
                    current_sum = nums[i] + nums[i+j] + nums[left] + nums[right]
                    if current_sum == target and len(set([i, i+j, left, right])) == 4:
                        quads.append([nums[i], nums[i+j], nums[left], nums[right]])
                        left +=1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        #As quads is a list of lists, we cannot use set() on it as set only works on tuples
        #So we turn each list in quads into a tuple, add that to a set, then list them
        quads = [list(tup) for tup in set(tuple(quad) for quad in quads)]
        return quads


        