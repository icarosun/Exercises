class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        m = len(nums1)
        n = len(nums2)

        if (n == 0 and m == 0):
            return 0

        middle = (m + n) // 2
        
        index = 0
        pivot_x = 0
        pivot_y = 0
        while (index <= middle and i < m and j < n):
            if nums1[i] < nums2[j]:
                value = nums1[i]
                i += 1
            else:
                value = nums2[j]
                j += 1
            if index == middle - 1:
                pivot_x = value
            if index == middle:
                pivot_y = value
            index += 1
        
        if (i < m or j < n):
            if (i < m):
                while (index <= middle):
                    value = nums1[i]
                    if index == middle - 1:
                        pivot_x = value
                    if index == middle:
                        pivot_y = value
                    i += 1
                    index += 1
            else:
                while (index <= middle):
                    value = nums2[j]
                    if index == middle - 1:
                        pivot_x = value
                    if index == middle:
                        pivot_y = value
                    j += 1
                    index += 1

        rest_middle = (m + n) % 2 
        if (rest_middle == 0):
            return (pivot_x + pivot_y) / 2
        else:
            return (pivot_y)
