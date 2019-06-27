"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""

from unittest import TestCase, main

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cutPoint = -1
        result = 0
        cache = {}
        for i, c in enumerate(s):
            if c in cache:
                result = max(i-cutPoint-1, result)
                cutPoint = max(cache[c], cutPoint)
            cache[c] = i
        return max(len(s)-cutPoint-1, result)

class Test(TestCase):
    def test(self):
        s = 'abcabcbb'
        sol = Solution()
        result = sol.lengthOfLongestSubstring(s)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    main()
