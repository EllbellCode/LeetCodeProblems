class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge the two arrays and sort them
        merged = sorted(nums1 + nums2)
        length = len(merged)
        
        # If the combined length is odd, return the exact middle element
        if length % 2 != 0:
            return float(merged[length // 2])
        
        # If the combined length is even, average the two middle elements
        else:
            mid1 = merged[length / 2 - 1]
            mid2 = merged[length / 2]
            return (mid1 + mid2) / 2.0



        