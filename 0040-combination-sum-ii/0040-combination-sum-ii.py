class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results =[]

        def backtrack(start, path, total):

            #base case
            if total == target:
                true_path = sorted(path[:])
                results.append(true_path)
                return

            #constraint
            if total > target:
                return

            #recursive
            prev = -1
            for i in range(start, len(candidates)):

                if candidates[i] == prev:
                    continue

                number = candidates[i]
                path.append(number)
                backtrack(i+1, path, total + number)
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return results
        