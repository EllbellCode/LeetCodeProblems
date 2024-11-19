class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x_str = str(x)
        str_list = []

        for char in x_str:
            str_list.append(char)
        str_list.reverse()

        if str_list[-1] == "-":
            str_list.pop()
            str_list = ["-"] + str_list
            
        str_rev = "".join(str_list)
        x_rev = int(str_rev)

        if -2**31 <= x_rev <= 2**31 - 1:
            return x_rev
        else:
            return 0

        
        