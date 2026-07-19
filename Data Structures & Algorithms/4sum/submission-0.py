class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            curr = [nums[i], nums[j], nums[k], nums[l]]
                            curr.sort()
                            if curr not in res:
                                res.append(curr)
        return res