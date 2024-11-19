class Solution(object):
    def convert(self, s, numRows):

        list_parts = []
        for i in range(numRows):
            list_parts.append([])

        step = 0
        direction = 0 # 0 for increment, 1 for decrement

        for i in range(len(s)):

            if numRows == 1:
                return s

            if step == numRows-1:
                direction = 1
            if step == 0:
                direction = 0

            if direction == 0:
                list_parts[step].append(s[i])
                step +=1
            else:
                list_parts[step].append(s[i])
                step -=1

        string_list = sum(list_parts, [])
        string = "".join(string_list)

        return string

        