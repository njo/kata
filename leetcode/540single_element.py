#  https://leetcode.com/problems/single-element-in-a-sorted-array/#/description


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)

        if ln == 0 or ln % 2 == 0:
            return None
        elif len(nums) == 1:
            return nums[0]

        # Look at the middle element and its 2 neighbours
        mid = ln / 2

        # partition the array to exclude mid and the number that matches
        if nums[mid] == nums[mid-1]:
            left = nums[:mid+1]
            right = nums[mid+1:]
        elif nums[mid] == nums[mid+1]:
            left = nums[:mid]
            right = nums[mid:]
        else:
            return nums[mid]

        if len(left) % 2 == 1:
            return self.singleNonDuplicate(left)
        return self.singleNonDuplicate(right)

print Solution().singleNonDuplicate([1, 1, 2])
print Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4])
print Solution().singleNonDuplicate([1, 1, 2, 2, 4, 4, 5, 5, 9])
