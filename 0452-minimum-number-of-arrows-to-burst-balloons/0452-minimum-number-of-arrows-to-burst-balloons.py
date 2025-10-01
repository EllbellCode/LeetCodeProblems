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

        This has O(n**2) complexity - we can do better!

        ORDER
        1: sort points on the index 1 of each element.
        2: Set the boundary to the earliest balloon end (now at index 0 in points)
        3: Set shot to 1 to account for the first balloon
        3: Iterate through points[1:], if a balloon has a greater start than our earliest end, we require another shot
        4: Increment shot, change our earliest balloon end to the end of the balloon we just shot
        5: return shots after iteration is complete

        This has O(NlogN) complexity from sorting the list at the start

        a<= x <=b
        x > b or a > x

        return incremented value
        """

        #Initialise to 1 to account for first shot at first balloon
        shots = 1

        #Sort balloons
        points.sort(key  = lambda x: x[1])

        earliest = points[0][1]

        for balloon in points[1:]:
              
            balloon_start = balloon[0]

            #If balloon start is greater than end of previous balloon
            #We need another shot to hit this balloon
            if balloon_start > earliest:
                 
                 shots +=1
                 
                 #Change our boundary to the end of the balloon we just shot
                 earliest = balloon[1]

        return shots
        
        shots = 0

        points.sort(key  = lambda x: x[1])

        while len(points) != 0:

            earliest = points[0][1]
                
            points = [x for x in points if x[0] > earliest or x[1] < earliest]
             
        
            shots +=1

        return shots









        