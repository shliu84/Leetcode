class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        (l, r) = (0, len(nums) - 1)
        if self.isBetween(nums, l, r, target) != -1:
            return self.isBetween(nums, l, r, target)
        else:
            return self.binary(nums, target, l, r)

    def binary(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l < r:
            mid = int((l + r) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binary(nums, target, mid + 1, r)
            else:
                return self.binary(nums, target, l, mid - 1)
        else:
            return l + 1

    def isBetween(self, nums, l, r, target):
        if r - l < 2:
            if nums[l] < target and target < nums[r]:
                return r
            if target < nums[l]:
                return l
            if target > nums[r]:
                return r + 1
        else:
            return -1

