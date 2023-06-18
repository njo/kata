from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        ret = set()
        for n in nums2:
            if n in nums1:
                ret.add(n)
        return ret

class Solution1:
    """
    With a "arrays are sorted, o(n), o(1) constraint"
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i1 = i2 = 0
        ret = []
        # progress through whichever array has the lowest number
        
        while i1 < len(nums1) and i2 < len(nums2):
            # If we match, add then move both pointers ahead to the next number
            if nums1[i1] == nums2[i2]:
                ret.append(nums1[i1])
                while i1 < len(nums1) and nums1[i1] == ret[-1]:
                    i1 += 1
                while i2 < len(nums2) and nums2[i2] == ret[-1]:
                    i2 += 1
                continue
            if nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return ret

print(Solution1().intersection([4,9,5], [9,4,9,8,4]))
