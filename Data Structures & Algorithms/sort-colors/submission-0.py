class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ls = [0] * 3
        k = 0
        for n in nums:
            ls[n] += 1
        for i in range(len(nums)):
            if ls[k] > 0:
                nums[i] = ls.index(ls[k])
                ls[k] -= 1
                if ls[k] == 0:
                    k += 1
        
