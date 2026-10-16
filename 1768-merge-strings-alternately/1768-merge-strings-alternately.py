class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        maxLen = max(len(word1),len(word2))
        comb = ""

        for i in range(maxLen):

            if i < len(word1):
                comb += word1[i]

            if i < len(word2):
                comb += word2[i]

        return comb
