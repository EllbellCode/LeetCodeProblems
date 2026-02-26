class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                totals = []
                if i > 0:
                    totals.append(grid[i-1][j])
                if j > 0:
                    totals.append(grid[i][j-1])

                if len(totals) > 0:
                    minimum = grid[i][j] + min(totals)
                    grid[i][j] = minimum

        return grid[-1][-1]
    

                
        