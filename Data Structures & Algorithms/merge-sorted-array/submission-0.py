class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 > n2:
                nums1[k] = n1
                i -= 1
            else:
                nums1[k] = n2
                j -= 1
            k -= 1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
        