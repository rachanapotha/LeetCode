class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the shorter array
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        total = m + n
        half = total // 2

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2          # cut in A
            j = half - i                 # cut in B

            Aleft = A[i-1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j-1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # Valid partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # odd
                    return float(min(Aright, Bright))
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            # Move cut
            if Aleft > Bright:
                hi = i - 1
            else:
                lo = i + 1

        