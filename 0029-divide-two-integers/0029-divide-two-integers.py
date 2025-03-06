class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # Handle cases of 1 and -1
        if divisor == 1:
            return min(max(-2**31, dividend), 2**31 - 1)
        if divisor == -1:
            return min(max(-2**31, -dividend), 2**31 - 1)

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Compute absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            #Use bit shifting to speed up subtraction process
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
        
            dividend -= temp
            quotient += multiple

    
        return min(max(-2**31, sign * quotient), 2**31 - 1)
        

       