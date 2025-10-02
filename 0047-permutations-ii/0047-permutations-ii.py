class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Backtracking


        place elements until list = length of nums
        
        """
        perms = []

        def tree(input, path=[]):

            if len(path) == len(nums): 
                perms.append(path)

            else:
                for i in range(len(input)):
                    
                    new = input[:i] + input[i+1:]
                    tree(new, path + [input[i]])

        tree(nums)

        perm_set = perm_set = {tuple(perm) for perm in perms}
        unique = [list(x) for x in perm_set]

        return unique


        