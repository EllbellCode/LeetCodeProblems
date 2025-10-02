class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        take each string
        order alphabetically
        anagrams will be the same

        """

        anagrams = {}

        for i in range(len(strs)):

            sorted_val = sorted(strs[i])
            join = "".join(sorted_val)


            if join in anagrams:
                  
                  anagrams[join].append(strs[i])

            if join not in anagrams:
                  
                  anagrams[join] = [strs[i]]


        anagram_list = list(anagrams.values())

        return anagram_list

