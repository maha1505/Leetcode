class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums:
            if target==i:
                return nums.index(i)
        return -1
