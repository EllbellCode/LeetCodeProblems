class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)  # Convert integer to string
        left, right = 0, len(x) - 1  # Pointers at both ends

        while left < right:
            if x[left] != x[right]:  # Check if characters match
                return False
            left += 1
            right -= 1
        return True


        