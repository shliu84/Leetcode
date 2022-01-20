class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            right = target-numbers[l]
            if right==numbers[r]:
                return l+1,r+1
            if right<numbers[r]:
                r = r -1
            else:
                if r+1 < len(numbers):
                    r = r + 1
                l = l + 1