class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if l > j + 1 and nums[l] == nums[l - 1]:
                        l += 1
                        continue
                    curr_target = target - nums[i] - nums[j]
                    curr_sum = nums[l] + nums[r]
                    if curr_target == curr_sum:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                    elif curr_target < curr_sum:
                        r -= 1
                        continue
                    l += 1
                    
        return res
                    