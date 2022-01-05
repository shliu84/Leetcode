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
        nums = list(range(n+1))
        self.ternary(nums, 1, n)


    def ternary(self, nums: List[int], l: int, r: int) -> int:
        if l < r:
            midleft = int((l + r) / 4)
            midright = midleft * 2
            print(midleft)

            if not isBadVersion(nums[midleft]) and isBadVersion(nums[midright]):
                if midleft == midright - 1:
                    return midright
                else:
                    return self.ternary(nums, midleft, midright)
            elif isBadVersion(nums[midleft]) and isBadVersion(nums[midright]):
                return self.ternary(nums, l, midleft)
            elif not isBadVersion(nums[midleft]) and not isBadVersion(nums[midright]):
                return self.ternary(nums,midright+1, r)
            else:
                print("error")
        else:
            return -1

        def isFirstBadVersion(n):
            if not isBadVersion(n-1) and isBadVersion(nums[n]):
                return true
            else:
                return false

def isBadVersion(n):
    if n >= 3:
        return True
    else:
        return False
