# https://leetcode.com/problems/3sum/#/description


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        zero = []
        pos = []
        neg = []

        for n in nums:
            if n < 0:
                neg.append(n)
            elif n > 0:
                pos.append(n)
            else:
                zero.append(0)

        pos.sort()
        neg.sort()
        results = []

        def gen():
            if len(zero) >= 3:
                yield [0, 0, 0]

            for pi, p in enumerate(pos):
                for ni, n in enumerate(neg):
                    if n + p == 0:
                        if len(zero) > 0:
                            yield [n, p, 0]
                    elif n + p < 0:
                        for pi2, p2 in enumerate(pos):
                            if pi2 == pi:
                                continue
                            if p2 + n + p > 0:
                                break
                            if p2 + n + p == 0:
                                yield [n, p, p2]
                    else:
                        for ni2, n2 in enumerate(neg):
                            if ni2 == ni:
                                continue
                            if n2 + n + p > 0:
                                break
                            if n2 + n + p == 0:
                                yield [n, p, n2]
        for result in gen():
            result.sort()
            if result not in results:
                results.append(result)

        return results

print Solution().threeSum([-1, 0, 1, 2, -1, -4])
