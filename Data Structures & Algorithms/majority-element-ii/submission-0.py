class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        l, r = 0, 0
        res = []
        x = len(nums) // 3
        while r < len(nums):
            curr = nums[l]
            while r < len(nums) and curr == nums[r]:
                r += 1
            if r - l > x:
                res.append(curr)
                l = r
            else:
                l += 1
        return res
