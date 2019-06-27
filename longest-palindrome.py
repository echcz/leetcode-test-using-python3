"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""

from unittest import TestCase, main

class StrCounter:
    def __init__(self, s: str, c: int = 1):
        self.s = s
        self.c = c

    def plusCount(self, c: int = 1):
        self.c += c

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return s
        cache = [StrCounter('01', 0)]
        for c in s:
            sc = cache[-1]
            if sc.s == c:
                sc.plusCount()
            else:
                cache.append(StrCounter(c))
        cache.append(StrCounter('02', 0))
        size = cache[1].c
        start = 1
        end = 2
        tmpSize = size
        for i in range(1, len(cache)-1):
            j = 1
            while True:
                a = cache[i-j]
                b = cache[i+j]
                if a.s == b.s:
                    if a.c == b.c:
                        tmpSize += a.c * 2
                        j += 1
                    else:
                        tmpSize += min(a.c, b.c) * 2
                        if tmpSize > size:
                            size = tmpSize
                            start = i - j
                            end = i + j + 1
                        tmpSize = cache[i+1].c
                        break
                else:
                    if tmpSize > size:
                        size = tmpSize
                        start = i - j + 1
                        end = i + j
                    tmpSize = cache[i+1].c
                    break
        h = cache[start]
        t = cache[end-1]
        c = min(h.c, t.c)
        h.c = c
        t.c = c
        result = ''
        for i in range(start, end):
            sc = cache[i]
            result += sc.s * sc.c
        return result

class Test(TestCase):
    def test(self):
        s = 'adabacabd'
        sol = Solution()
        reulst = sol.longestPalindrome(s)
        self.assertEqual(reulst, 'bacab')

if __name__ == '__main__':
    main()
