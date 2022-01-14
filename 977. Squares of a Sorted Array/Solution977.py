#https://www.youtube.com/watch?v=FPCZsG_AkUg

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        arr = []
        while l<=r:
            sql = nums[l]*nums[l]
            sqr = nums[r]*nums[r]
            if sql < sqr:
                r = r-1
                arr.append(sqr)              
            else:
                l = l+1
                arr.append(sql)
        return arr[::-1]
    