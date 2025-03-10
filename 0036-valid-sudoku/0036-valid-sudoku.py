class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):

            #filter out empty tiles
            row_elements = [num for num in board[i] if num != "."]
            col_elements = [board[j][i] for j in range(9) if board[j][i] != "."]

            #check uniqueness
            if len(row_elements) != len(set(row_elements)) or len(col_elements) != len(set(col_elements)):

                return False

        #could also use loop over range(0,9,3) for the subgruds
        subgrids = [(0,0), (0,3), (0,6),
                    (3,0),  (3,3),  (3,6),
                     (6,0),  (6,3),  (6,6)]

        for subgrid in subgrids:

            row, col = subgrid
            elements = []

            #obtain elements in subgrid
            for i in range(3):
                for j in range(3):
                    elements.append(board[row+i][col+j])

            elements_rem = [num for num in elements if num != "."]

            #check uniqueness
            if len(elements_rem) != len(set(elements_rem)):
                return False

        return True

            

