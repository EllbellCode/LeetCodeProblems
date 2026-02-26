class Solution(object):
    def generateMatrix(self, n):
        
    
        init = 1
        row = 0
        column = 0
        start = 0
        end = n

        positions = {}
        while init <= n**2:

            if init > n**2:
                break

            # Right
            while column < end:

                positions[row,column] = init
                column += 1
                init += 1
            if init > n**2:
                break

            column -= 1
            row += 1

            # Down
            while row < end:

                positions[row,column] = init
                row += 1
                init += 1
            if init > n**2:
                break

            row -= 1
            column -= 1

            # Left
            while column >= start:

                positions[row,column] = init
                column -= 1
                init += 1
            if init > n**2:
                break

            column += 1
            row -= 1
            start += 1

            # Up
            while row >= start:

                positions[row,column] = init
                row -= 1
                init +=1
            if init > n**2:
                break

            row += 1
            column += 1
            end -= 1

        print(positions)

        grid = []

        for i in range(n):
            row = []
            for j in range(n):

                row.append(positions[i,j])

            grid.append(row)

        return grid
