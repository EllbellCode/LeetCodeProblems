class Solution(object):
    def generateMatrix(self,n):

        import numpy as np 
        
        init = 1
        row = 0
        column = 0
        start = 0
        end = n
        grid = np.zeros((n,n), dtype=int)
        print(grid[0,0])

        positions = {}
        while init <= n**2:

            if init > n**2:
                break

            # Right
            while column < end:

                grid[row,column] = init
                column += 1
                init += 1
            if init > n**2:
                break

            column -= 1
            row += 1

            # Down
            while row < end:

                grid[row,column] = init
                row += 1
                init += 1
            if init > n**2:
                break

            row -= 1
            column -= 1

            # Left
            while column >= start:

                grid[row,column] = init
                column -= 1
                init += 1
            if init > n**2:
                break

            column += 1
            row -= 1
            start += 1

            # Up
            while row >= start:

                grid[row,column] = init
                row -= 1
                init +=1
            if init > n**2:
                break

            row += 1
            column += 1
            end -= 1

        return grid.tolist()
