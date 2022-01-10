class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        (l, r) = (0, len(nums) - 1)
        return self.binary(nums, target, l, r)

    def binary(self, nums: List[int], target: int, l: int, r: int) -> int:
        if target <= nums[l]:
            return l
        if target > nums[r]:
            return r + 1

        if l < r:
            mid = int((l + r) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binary(nums, target, mid + 1, r)
            else:
                return self.binary(nums, target, l, mid - 1)
        else:
            return -1
