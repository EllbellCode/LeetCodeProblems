class Solution(object):
    def letterCombinations(self, digits):

        if digits == "":
            return []

        import itertools

        letters = {1: [''], 2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'], 
                    5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r', 's'], 
                   8: ['t','u','v'], 9: ['w','x','y', 'z']}

        digit_letters = []
        combinations = []

        for char in digits:
            digit_letters.append(letters[int(char)])

        #Cartesian Product over all of the lists
        #To give every combination!
        for element in itertools.product(*digit_letters):
            combinations.append(''.join(element))

        return combinations