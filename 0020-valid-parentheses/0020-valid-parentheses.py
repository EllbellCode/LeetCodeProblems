class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        #Map of close to open brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:

            #If char is a close bracket
            if char in bracket_map:
                
                #If stack is not empty
                if stack:
                    #set top element to be the last element
                    # which is the least nested open bracket
                    top_element = stack.pop()
                
                else:
                    #else store a dummy variable to fail the next if gate
                    top_element = "#"
                
                #If the characters do not match then
                #The brackets are not nested correctly
                if bracket_map[char] != top_element:  
                    return False
            
            else:
                stack.append(char)

        # Stack should be empty if all brackets are properly closed
        return not stack


        