class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) > len(str2):
            strLong = str1
            strShort = str2
        else:
            strLong = str2
            strShort = str1

        substrings = []
        substring = ""
        for char in strShort:
            substring += char
            substrings.append(substring)

        answer = ""
        for substring in substrings:
            multipleLong = len(strLong)/len(substring)
            multipleShort = len(strShort)/len(substring)

            if multipleLong % 1 == 0 and multipleShort % 1 == 0:

                stringLong = substring*multipleLong
                stringShort = substring*multipleShort

                if stringLong == strLong and stringShort == strShort :
                    answer = substring

        return answer

            

        
        
        