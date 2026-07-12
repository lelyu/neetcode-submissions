class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key, value in c.items():
            if value > len(nums) // 2:
                return key
        return -1