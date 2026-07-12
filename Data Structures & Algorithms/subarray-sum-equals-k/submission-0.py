class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix  = defaultdict(int)
        curr_sum = 0
        res = 0
        for n in nums:
            curr_sum += n
            if curr_sum == k:
                res += 1
            if curr_sum - k in prefix:
                res += prefix[curr_sum - k]
            prefix[curr_sum] += 1
        return res