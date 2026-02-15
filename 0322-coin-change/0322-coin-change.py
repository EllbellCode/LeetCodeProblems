class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # Create an array of size (amount + 1) to store our answers.
        # Default everything to infinity.
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0
        
        # Iterate through every amount from 1 up to the target amount
        for a in range(1, amount + 1):
            # Try every available coin
            for coin in coins:
                # Check if the current coin can be used
                if a - coin >= 0:
                    # Update the DP array:
                    # Do we keep the current known minimum for this amount, 
                    # or is it better to use 1 of this current coin + the minimum coins needed for the remainder?
                    dp[a] = min(dp[a], 1 + dp[a - coin])
                    
        # If the target amount is still infinity, it means no combination worked
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

                



            




        