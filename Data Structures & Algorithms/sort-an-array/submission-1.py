class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        max_val = max(nums)
        min_val = min(nums)
        pos = [0] * (max_val + 1)
        neg = [0] * (abs(min_val) + 1)

        for i in nums:
            if i >= 0:
                pos[i] += 1
            else:
                neg[abs(i)] += 1

        for i in reversed(range(len(neg))):
            if neg[i] > 0:
                for j in range(neg[i]):
                    res.append(-i)
        
        for i in range(len(pos)):
            if pos[i] > 0:
                for j in range(pos[i]):
                    res.append(i)
        return res
        
            