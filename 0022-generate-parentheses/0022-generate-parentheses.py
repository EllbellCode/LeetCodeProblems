class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        results = []
        max_length = 2*n

        def recurse(current_string, open, close, n):

            if len(current_string) == max_length:
                results.append(current_string)

            if open < n:
                new_string = current_string + "("
                recurse(new_string, open+1, close, n)

            if close < open:
                new_string = current_string + ")"
                recurse(new_string, open, close+1, n)

        recurse("", 0, 0, n)

        return results



        