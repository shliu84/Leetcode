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
        
        # method 4 failed
        # def n_Left_Rotate_k_Time (nums, n, k):
        #     for x in range (k):
        #         nums[n-1],nums[n] = nums[n],nums[n-1]
        #         n = n - 1
            
        # k = k % len(nums)    
        # l = len(nums) - k
        # for i in range (l, len(nums)):
        #     n_Left_Rotate_k_Time(nums, i, l)
        
        # return nums


        #method 5 https://youtu.be/BHr381Guz3Y
        def reverse(nums, l, r):
            while l<r:
                nums[l],nums[r] = nums[r], nums[l]
                l=l+1
                r=r-1
        k = k % len(nums)
        reverse(nums,0, len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k, len(nums)-1)