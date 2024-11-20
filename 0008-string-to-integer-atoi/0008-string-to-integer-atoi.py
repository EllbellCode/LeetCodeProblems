class Solution(object):
    def myAtoi(self, s):
        
        s = s.lstrip(" ")

        if len(s) == 0:
            return 0
        
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1

        s = s.lstrip("0")

        number_str = ""

        for char in s:
            if char.isdigit():
                number_str += char
            else:
                break

        if number_str == "":
            number_str = "0"

        number_int = int(number_str) * sign

        if number_int < -2**31:
            number_int = -2**31
        elif number_int > 2**31 - 1:
            number_int = 2**31 - 1

        return number_int
           

        

        