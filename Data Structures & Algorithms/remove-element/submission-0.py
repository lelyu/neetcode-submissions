class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while i + k < len(nums):
            if nums[i] == val:
                nums[i], nums[len(nums) - 1 - k] = nums[len(nums) - 1 - k], nums[i]
                k += 1
                continue
            i += 1
        return i
