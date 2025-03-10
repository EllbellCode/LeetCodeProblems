class Solution(object):
    def countAndSay(self, n):

        string = "1"

        for _ in range(n-1):

            new_string = ""
            count = 1

            for i in range(1, len(string)):
                if string[i] == string [i-1]:
                    count += 1

                else:

                    new_string += str(count) + string[i-1]
                    count = 1
            
            new_string += str(count) + string[-1]
            string = new_string

        return string







