class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # We are looking to calculate x**n
        # Naive approach is to simply return x**n
        # This will actually work as pythons power operation is optimised
        # So assume we cannot do this
        # The best way is modular exponentiati
        
        # If n is even, set x = x*x and divide n by 2
        # If n is odd, subtract 1 from n, multiply a counter by x then repeat n even step
        
        remainder = 1
        neg = False

        if n == 0:
            return 1

        if n < 0:
            neg = True
            n = abs(n)

        while n > 1:

            if n % 2 == 0:

                x = x*x
                n = n//2

            elif n % 2 == 1:

                remainder = remainder*x
                n = n - 1

        if neg:
            return 1/(x*remainder)
        else:
            return x*remainder
        