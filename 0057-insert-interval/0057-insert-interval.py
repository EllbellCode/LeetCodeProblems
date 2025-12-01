class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        result = []
        i = 0
        n = len(intervals)
        
        # STAGE 1: The Left (No Overlap)
        # Add all intervals that end BEFORE the newInterval starts.
        # Logic: If current_end < new_start, it's strictly to the left.
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # STAGE 2: The Merge (The "Snowball")
        # While we are overlapping, keep merging intervals.
        # Logic: We know they overlap if the current_start <= new_end.
        while i < n and intervals[i][0] <= newInterval[1]:
            # Update the bounds of the newInterval (The "Snowball" grows)
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # After the merge loop finishes, add the fully merged interval
        result.append(newInterval)
        
        # STAGE 3: The Right (No Overlap)
        # Add the remaining intervals that start AFTER the newInterval ends.
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result



                







        












    
        