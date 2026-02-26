class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 1
        notFound = True
        word = ""
        wordStart = False

        while i <= len(s) and notFound:
            # only start adding letters after first non space character

            if s[-i] != " " and not wordStart:
                word += s[-i]
                wordStart = True

            elif s[-i] == " " and wordStart:

                notFound = False

            elif s[-i] != " " and wordStart:
                word += s[-i]

            i += 1

        return len(word)


 
        