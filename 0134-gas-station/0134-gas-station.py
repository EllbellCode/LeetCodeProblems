class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        """

        if sum(gas) < sum(cost):

            return -1
            
        index = 0

        tank = 0

        for i in range(len(gas)):

            net_gain = gas[i] - cost[i]

            tank += net_gain

            if tank < 0:

                tank = 0
                #We can skip to index i + 1 here is we know every index before this was positive 
                #(otherwise we would not have reached this index)
                index = i + 1

        return index
        