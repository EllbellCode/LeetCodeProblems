class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #Loop over letters of first word
        for i in range(len(strs[0])):
            
            letter = strs[0][i]   
            
            #Compare with rest of words
            for word in strs[1:]:
                
                # If exceeds number of letters in word or letters do not match
                if i >= len(word) or word[i] != letter:

                    # Return common prefix up to this point
                    return strs[0][:i]
                    
        # If loop completes, first word is the prefix
        return strs[0]
    
        

            
            







