class Solution(object):
    def intToRoman(self, num):
        
        #Couples of numerals and their values
        roman_numerals = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]

        #Iterate through numbers and subtract from num until it is
        #less than the numeral then move on to the next numeral

        #This only works if num < 3999 as 4000 would be represented by I(10000 symbol)
        #Which is not in our set
        result = []
        for roman, value in roman_numerals:
            while num >= value:
                result.append(roman)
                num -= value

        return ''.join(result)
        
       

            


            



        