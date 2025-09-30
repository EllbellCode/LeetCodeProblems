class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #stores all of the permutations
        results = []
        #current path being built
        path = []

        used = [False] * len(nums)

        def backtrack():

            #Path has been built so append to results
            if len(path) == len(nums):
                results.append(list(path))
                return


            for i in range(len(nums)):
                
                #If number has not yet been used in this path
                if not used[i]:
                    
                    #Add to path
                    path.append(nums[i])
                    #Change used to true so we know it has been used
                    used[i] = True

                    #recursively backtrack
                    #Now, when we come to use the same element we will skip it as it is marked True in used
                    #Will do these until all values have been used and marked true
                    backtrack()

                    #Removes the last element from the path
                    path.pop()

                    used[i] = False

        backtrack()

        return results


"""
EXAMPLE

initial call to backtrack()
empty permutation list, path=[]

The outermost loop starts at i=0 and selects 1.
path becomes [1], and 1 is marked used.
backtrack() is called again. (depth 1).

The inner loop (depth 1) skips 1 and selects 2 (i=1).
path becomes [1,2], and 2 is marked used.
backtrack() is called again. (depth 2).

The innermost loop (depth 2) skips 1 and 2, and selects 3 (i=2).
path becomes [1,2,3], and 3 is marked used.
backtrack() is called again. (We are now at depth 3).

The function immediately detects that len(path) is 3.
[1,2,3] is added to the results. The function returns to depth 2.

We return to the inner loop that chose 3.
3 is popped from path, which reverts to [1,2]. 3 is marked unused.
The loop finishes its iteration (no more numbers left to try at this depth).
Nothing is added to results
The function returns to depth 1.

We return to the loop that chose 2.
2 is popped from path, which reverts to [1]. 2 is marked unused.
The loop continues from where it left off (i=2) and selects 3.
path becomes [1,3], and 3 is marked used.
backtrack() is called.
The innermost loop (at depth 2) skips 1 and 3, and selects 2.
path becomes [1,3,2], and 2 is marked used.
backtrack() is called.
The function detects the full length.
[1,3,2] is added to the results. The function returns.

Repeat this process for popping 1 in i=0 to get all permutations!


"""


        



        