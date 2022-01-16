class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
                
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != 0:
                left = left + 1
            right = right + 1