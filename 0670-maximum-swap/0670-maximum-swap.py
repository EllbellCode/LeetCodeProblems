class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int

        Convert to string
        go digit by digit
        if there is a digit bigger than the current digit we are on, swap with the RIGHTMOST occurence
        if not, move to next digit
        """

        num_str = str(num)
        num_lst = list(num_str)

        for i in range(len(num_str)-1):

            max_val = max(num_str[i+1:])

            if num_str[i] < max_val:

                #Find the RIGHTMOST occurrence of max_val 
                max_index =len(num_str)-1-num_str[::-1].index(max_val)

                num_lst[i], num_lst[max_index] = num_lst[max_index], num_lst[i]

                return int("".join(num_lst))

        return num




        