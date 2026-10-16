class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbeds_zero = [[1], [1,0], [0,1]]
        flowerbeds_one = [[0], [0,0]]
        if flowerbed in flowerbeds_zero:
            return n <= 0
        if flowerbed in flowerbeds_one:
            return n <= 1    

        count = 0
        for i in range(len(flowerbed)-2):

            j= i+1
            k = i+2

            if i == 0:
                if flowerbed[i] == 0 and flowerbed[j] == 0:
                    count += 1
                    flowerbed[i] = 1
            
            if k == len(flowerbed)-1:
                if flowerbed [k] == 0 and flowerbed[j] == 0:
                    count +=1
                    flowerbed[k] = 1
            
            if flowerbed [k] == 0 and flowerbed[j] == 0 and flowerbed[i] == 0:
                    count +=1
                    flowerbed[j] = 1
            
        if count >= n:
            return True
        else:
            return False
        