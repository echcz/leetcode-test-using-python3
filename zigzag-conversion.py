"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串。
"""

from unittest import TestCase, main

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        cache = ["" for x in range(numRows)]
        flag = True
        i = 0
        for c in s:
            cache[i] += c
            i += 1 if flag else -1
            if i < 0 or i >= numRows:
                i = numRows-2 if flag else 1
                flag = not flag
        return ''.join(cache)

class Test(TestCase):
    def test(self):
        s = 'PAYPALISHIRING'
        numRows = 3
        sol = Solution()
        result = sol.convert(s, numRows)
        self.assertEqual('PAHNAPLSIIGYIR', result)

if __name__ == '__main__':
    main()
