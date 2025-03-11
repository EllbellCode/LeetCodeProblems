class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        
        def backtrack(start, path, total):

            #Add path to results if we have hit target
            if total == target:
                result.append(path[:])  
                return
            
            # stop recursion if we have exceeded target
            if total > target:
                return

            #choose next element to add
            for i in range(start, len(candidates)):  
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  
                path.pop()  #remove candidates[i] from path to try next element

        backtrack(0, [], 0)
        return result        