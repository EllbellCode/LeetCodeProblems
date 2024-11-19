class Solution(object):
    def longestPalindrome(self, s):

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
        # Return the palindrome substring (excluding the last expanded invalid indices)
            return s[left+1:right]
            
        if not s:
            return ""
    
        longest = ""
    
        for i in range(len(s)):
        # Odd-length palindromes: expand around the single character
            palindrome1 = expand_around_center(i, i)
        # Even-length palindromes: expand around the pair of characters
            palindrome2 = expand_around_center(i, i + 1)
        
        # Update the longest palindrome if a new longer one is found
            longest = max(longest, palindrome1, palindrome2, key=len)
    
        return longest


        