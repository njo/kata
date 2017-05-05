class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        to_get = (len(nums1) + len(nums2)) % 2 or 2
        p1 = len(nums1) / 2
        p2 = len(nums2) / 2
        bigger = len(nums1) - p1 - 1
        smaller = p1


        # we know that half the numbers in the first array are bigger and half are smaller
        # binary search the second array until half are bigger and half are smaller in total
        
        # What if we hit a boundary?


        # if both are odd or even we need 2 numbers to average
        # else just need one number
        
        
        
        
        