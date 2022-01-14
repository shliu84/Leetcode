class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         # method 1 (too slow)
#         def rotateOneTime (nums):
#             for i in range (len(nums)-1,0,-1):
#                 nums[i-1],nums[i] = nums[i],nums[i-1]
#             return nums
        
#         for i in range (k):
#             rotateOneTime(nums)

        ##method 2 (not working for leetcode, too much space?)
        # nums = nums[-k:] + nums[:-k]
        # return nums
        
        ##method 3 not working
        # def rotateOneTime (nums):
        #     nums = [nums[-1]]+nums[:-1]
        #     return nums
        # for i in range (k):
        #     nums = rotateOneTime(nums)
        
        
        def n_Left_Rotate_k_Time (nums, n, k):
            for x in range (k):
                nums[n-1],nums[n] = nums[n],nums[n-1]
                n = n - 1
            
        k = k % len(nums)    
        l = len(nums) - k
        for i in range (l, len(nums)):
            n_Left_Rotate_k_Time(nums, i, l)
        
        # return nums
        