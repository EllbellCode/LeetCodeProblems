class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        Turn row 0 to column n
        row 1 to column n-1...

        turn row i into column n-i

        1: (0,0) -> (0,n)
        2: (0,1) -> (1,n)
        3: (0,2) -> (2, n)
         ....
        n: (0,n) -> (n,n)

        METHOD:

        extract each row
        """

        n = len(matrix)

        # Step 1: Transpose the matrix
        # Iterate through the upper triangle of the matrix
        for i in range(n):
            for j in range(i, n):
                # Swap the elements matrix[i][j] and matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

        return matrix

        