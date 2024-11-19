class Solution(object):
    def convert(self, s, numRows):

        # If numRows = 1 then it is just the same string
        # If numRows >= len(s) then it will just be a vertical column and so the same string
        if numRows == 1 or numRows >= len(s):
                return s

        zigzag = [''] * numRows
        current_row = 0
        going_down = False

        # Go through each character in s and assign it to one of the 4 rows
        # increment/decrement depending on if you are going up or down in the zigzag
        for char in s:
            
            # add char to the correct row string
            zigzag[current_row] += char

            # change direction once you reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to the next row
            current_row += 1 if going_down else -1

        # combine row strings
        return "".join(zigzag)

        