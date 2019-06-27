"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
"""

from unittest import TestCase, main
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        i = 0
        v = nums[0]
        count = 1
        while i + v < length - 1:
            maxVal = 0
            tmpI = i
            for j in range(1, nums[i]+1):
                val = nums[tmpI+j] + j
                if val > maxVal:
                    maxVal = val
                    i = j + tmpI
            v = nums[i]
            count += 1
        return count

class Test(TestCase):
    def test(self):
        nums = [3, 1, 1, 1, 1]
        sol = Solution()
        result = sol.jump(nums)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    main()
