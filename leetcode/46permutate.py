#  https://leetcode.com/problems/permutations/#/solutions


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def perms(l):
            if len(l) == 1:
                return [l]
            ret = []
            head = l[:1]
            for tail in perms(l[1:]):
                for i in range(len(l)):
                    ret.append(tail[:i] + head + tail[i:])
            return ret

        return perms(nums)

print Solution().permute([1, 2, 3])
