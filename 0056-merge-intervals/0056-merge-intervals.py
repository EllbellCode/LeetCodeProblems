class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # If the list of merged intervals is empty 
            # OR if the current interval does not overlap with the previous one,
            # simply append it.
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap, so we merge the current and previous intervals.
                # We do this by updating the end time of the previous interval 
                # to be the maximum of the two end times.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


        



            





        