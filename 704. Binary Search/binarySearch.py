class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = int(len(nums)/2)
        if nums[mid] == target:
            return mid

        if mid == 0:
            return -1

        elif nums[mid] > target:
            return search(nums[0:mid], target)

        else:
            return search(nums[0:mid], target)

nums = [-1,0,3,5,9,12]
target = 9


