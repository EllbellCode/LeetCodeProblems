class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        memo = {}

        def newrecurse(rem):
            # 1. Look up the answer in the cache first
            if rem in memo:
                return memo[rem]

            # Base Cases
            if rem == 0:
                return 0  
            if rem < 0:
                return float('inf') 

            min_steps = float('inf')

            # Try every coin
            for coin in coins:
                steps = newrecurse(rem - coin)
                
                if steps != float('inf'):
                    min_steps = min(min_steps, steps + 1)

            # 2. Save the calculated answer to the cache BEFORE returning
            memo[rem] = min_steps
            return min_steps

        # Trigger the recursion
        minsteps = newrecurse(amount)
        
        # Return -1 if impossible, otherwise return the steps
        if minsteps == float('inf'):
            return -1
        else:
            return minsteps

                



            




        