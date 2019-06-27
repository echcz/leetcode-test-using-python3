"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""

from unittest import TestCase, main
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       numDict = {}
       for index, num in enumerate(nums):
           otherNum = target - num
           if otherNum in numDict:
               return [numDict[otherNum], index]
           numDict[num] = index

class Test(TestCase):
    def test(self):
        nums = [1, 2, 3, 4, 5]
        target = 8
        sol = Solution()
        result = sol.twoSum(nums, target)
        self.assertEqual(result, [2, 4])

if __name__ == '__main__':
    main()
