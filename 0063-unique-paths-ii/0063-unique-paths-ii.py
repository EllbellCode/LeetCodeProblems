class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[-1][-1] == 1:
            return 0
            
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        grid = [[0] * n for _ in range(m)]

        grid[0][0] = 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                total = 0

                if j > 0 and obstacleGrid[i][j-1] != 1:
                    total += grid[i][j-1]

                if i > 0 and obstacleGrid[i-1][j] != 1:
                    total += grid[i-1][j]

                if  not (i == 0 and j ==0):

                    grid[i][j] = total

        return grid[-1][-1]



        