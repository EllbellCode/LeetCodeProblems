class Solution(object):
    def lengthOfLongestSubstring(self, s):

        characters = []
        longest_length = 0

        for i in range(len(s)):

            if s[i] in characters: #If s is already in the sequence, start again
                characters = characters[characters.index(s[i])+1:]
            
            characters.append(s[i])

            if len(characters) > longest_length: #If the current sequence is longer than the current longest, replace
                longest_length = len(characters)
        
        return longest_length

        