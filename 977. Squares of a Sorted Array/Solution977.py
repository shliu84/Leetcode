class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        arr=[]
        arr = [-1] * len(nums)
        for i in range(r,-1,-1):
            if l == r:
                arr[i] = nums[l]*nums[l]
                break
            (l,r,sq) = self.nextSquare(nums,l,r)
            arr[i] = sq
        return arr
    
    def nextSquare(self, nums, l, r):
        if abs(nums[l]) < abs(nums[r]):
            return (l, r-1, nums[r]*nums[r])
        else:
            return (l+1, r, nums[l]*nums[l])