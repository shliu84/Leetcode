# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

from typing import List

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binary(1, n)

    def binary(self, l: int, r: int) -> int:
        if l <= r:
            mid = int((l + r) / 2)
            if self.isFirstBadVersion(mid):
                return mid
            elif isBadVersion(mid):
                return self.binary(l, mid - 1)
            else:
                return self.binary(mid + 1, r)
        else:
            return -1

    def isFirstBadVersion(self, n):
        if n - 1 > 0:
            if not isBadVersion(n - 1) and isBadVersion(n):
                return True
            else:
                return False
        else:
            if isBadVersion(n):
                return True
            else:
                print("There are not bad version.")
                return False

def isBadVersion(n):
    if n >= 3:
        return True
    else:
        return False
