class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # Start at 0,0
        # Iterate right 0,0 0,1 0,2 .... 0,n
        # iterate down 0,n 1,n 2,n .... m,n
        # iterate left m,n m,n-1 m,n-2 ... m,0 
        # iterate up m,0 m-1,0 .... 1,0

        # After iterating right/Left, we have taken a row out of the equation, so reduce m by 1
        # After iterating up/down, we take a column out, so reduce n by 1

        m = len(matrix)
        n= len(matrix[0])
        spiral = []

        while m > 1 and n > 1:

            # Right
            spiral.append(matrix[0])
            matrix.pop(0)
            m -= 1
            # Down
            for i in range(len(matrix)):
                spiral.append(matrix[i][-1])
                matrix[i].pop(-1)
            n -= 1
            # Left
            spiral.append(matrix[-1][::-1])
            matrix.pop(-1)
            m -= 1
            # Up
            for i in range(len(matrix)):
                spiral.append(matrix[len(matrix)-1-i][0])
                matrix[len(matrix)-1-i].pop(0)
            n -= 1

        spiral.append(matrix)

        def flatten_recursive(nested_list):
            flat_list = []
            for item in nested_list:
                if isinstance(item, list):
                    # Recursively call the function if the item is a list
                    flat_list.extend(flatten_recursive(item))
                else:
                    # Append the integer if it's not a list
                    flat_list.append(item)
            return flat_list

        #
        return flatten_recursive(spiral)




        