# https://leetcode.com/problems/palindrome-number/#/description
# "without extra space" taken to mean no additional variable assignments..
# which the string solution doesn't do either but what the hell

from math import log10 as log


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Totally valid solution :P
        # return x > -1 and str(x) == str(x)[::-1]

        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == x / pow(10, int(log(x))):  # first and last are the same
            x /= 10  # Remove the last digit

            # check the second digit isn't 0
            if x > 9 and x % pow(10, int(log(x))) < pow(10, int(log(x))-1):
                # It is, make sure the last one is zero too
                if x % 10 != 0:
                    return False

                # add a 1 to the second from the start and end
                x += pow(10, int(log(x))-1)
                x += 1

            x = x % pow(10, int(log(x)))  # remove the first digit

            return Solution().isPalindrome(x)

        return False


if __name__ == "__main__":
    import fileinput

    for line in fileinput.input():
        print Solution().isPalindrome(int(line))
