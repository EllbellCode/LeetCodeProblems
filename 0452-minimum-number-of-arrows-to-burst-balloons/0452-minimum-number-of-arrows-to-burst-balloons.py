class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        #Greedy Algorithm
        #Shoot arrow at the earliest ending point of a balloon

        """
        ORDER
        1: In the existing list, find the earliest ending point
        2: Record this and remove that balloon and any other balloon that would contain the coordinate
        3: Increment number of shots

        Repeat 1,2,3 on new list until list is empty

        a<= x <=b
        x > b or a > x

        return incremented value
        """

        
        shots = 0

        points.sort(key  = lambda x: x[1])

        while len(points) != 0:


            #earliest = 2**31
             
            #for x in points:

                #earliest = min(earliest, x[1])

            earliest = points[0][1]
                
            points = [x for x in points if x[0] > earliest or x[1] < earliest]
             
        
            shots +=1

        return shots









        