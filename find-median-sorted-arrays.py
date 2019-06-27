"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
"""

from unittest import TestCase, main
from typing import List, TypeVar, Generic

T = TypeVar('T')

class ListView:
    """
    列表只读视图，用于限定可访问元素
    """
    def __init__(self, l: List[T]):
        self.__c = 0
        self.__l = l

    def get(self, i: int) -> T:
        return self.__l[self.__c + i]

    def moveCursor(self, v: int):
        self.__c += v

    def isEnd(self) -> bool:
        return self.__c >= len(self.__l)

    def getTailCount(self) -> int:
        return len(self.__l) - self.__c

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        lenSum = len1 + len2
        flag = lenSum % 2 != 0
        if not len1:
            mid = len2 // 2
            return nums2[mid] if flag else (nums2[mid] + nums2[mid-1]) / 2
        if not len2:
            mid = len1 // 2
            return nums1[mid] if flag else (nums1[mid] + nums1[mid-1]) / 2
        mid1 = (lenSum-1) // 2
        lv1 = ListView(nums1)
        lv2 = ListView(nums2)
        while mid1 > 0 and (not lv1.isEnd()) and (not lv2.isEnd()):
            i = (mid1-1) // 2
            x = min(i+1, lv1.getTailCount(), lv2.getTailCount())
            n1 = lv1.get(x-1)
            n2 = lv2.get(x-1)
            if n1 < n2:
                lv1.moveCursor(x)
            else:
                lv2.moveCursor(x)
            mid1 -= x
        if lv1.isEnd():
            return lv2.get(mid1) if flag else (lv2.get(mid1) + lv2.get(mid1+1)) / 2
        if lv2.isEnd():
            return lv1.get(mid1) if flag else (lv1.get(mid1) + lv1.get(mid1+1)) / 2
        a = lv1.get(0)
        b = lv2.get(0)
        result1 = a
        if a < b:
            lv1.moveCursor(1)
        else:
            result1 = b
            lv2.moveCursor(1)
        if flag:
            return float(result1)
        else:
            if lv1.isEnd():
                return (result1 + lv2.get(0)) / 2
            elif lv2.isEnd():
                return (result1 + lv1.get(0)) / 2
            else:
                return (result1 + min(lv1.get(0), lv2.get(0))) / 2

class Test(TestCase):
    def test(self):
        nums1 = [1, 2, 3]
        nums2 = [3, 4, 5, 6, 7]
        sol = Solution()
        result = sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 3.5)

if __name__ == '__main__':
    main()
