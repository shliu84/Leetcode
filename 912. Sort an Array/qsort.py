class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        else:
            l = 0
            r = len(nums)-1
            nums = self.qsort(nums,l,r)
            return nums

    def qsort(self, nums,l,r):
        if l<r:
            i = self.partition(nums,l,r)
            self.qsort(nums,l,i-1)
            self.qsort(nums,i+1,r)
            return nums
        else:
            return nums

    def partition(self, nums, l, r):
        # rand = random.randint(l,r)
        # nums[rand], nums[r] = nums[r], nums[rand]
        pivot = nums[r]
        i = l - 1

        for j in range(l,r):
            if nums[j] <= pivot:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[r] = nums[r], nums[i+1]
            return i+1
