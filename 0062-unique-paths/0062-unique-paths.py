class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        dynamic programming

        Every step the robot takes, look at the steps it took to get there

        let our dp table be mxn. All values initialise to 0
        where dp[x][y] is the number of unique paths to reach x-1,y-1
        we start with dp[0][0] = 1 (only one way as this is where we start)

        then for example we look at dp[0][1]
        if m or n is less than 0, we can subtract to the step before it
        In this case we go to dp[0][0].
        We know there is only one way to get here so there must be only one way to get to [0][1]

        dp[1,1] for example
        this can be preceeded by [1][0] or [0][1]
        there is only 1 path to each of these so there is two total to this
        """

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                if i == 0  and j == 0:
                    # print("Init")
                    dp[i][j] = 1
                    print(dp)

                else:

                    if i > 0:
                        # print("Going Left")
                        left = dp[i-1][j]
                    else:
                        left = 0

                    if j > 0:
                        # print("Going Up")
                        up = dp[i][j-1]
                    else:
                        up = 0

                    dp[i][j] = left + up

        return dp[m-1][n-1]

                
                





                

        