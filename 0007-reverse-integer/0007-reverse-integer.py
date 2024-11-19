class Solution(object):
    def reverse(self, x):
        
        if x >=0:
            sign = 1
        else:
            sign = -1

        x = abs(x)

        x_rev = int(str(x)[::-1]) * sign

        if -2**31 <= x_rev <= 2**31 - 1:
            return x_rev
        else:
            return 0

        
        