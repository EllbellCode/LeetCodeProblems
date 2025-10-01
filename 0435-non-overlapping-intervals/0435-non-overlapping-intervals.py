class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        Approach

        Order on index 1 of the lists
        For lists with the same index 1, order then on index 0
        
        iterate through the list
        Start with index 1 from intervals[0] and compare it to index 0 of the next list
        If it is less than intervals[0][1] then there is an overlap
        increment remove value
        Move on to the next
        """

        removals = 0

        intervals.sort(key=lambda x: (x[1],x[0]))

        boundary = intervals[0][1]

        for interval in intervals[1:]:

            interval_start = interval[0]

            if interval_start < boundary:

                removals +=1

            else:

                boundary = interval[1]

        return removals


