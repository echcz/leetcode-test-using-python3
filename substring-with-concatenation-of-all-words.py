"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
"""

from unittest import TestCase, main
from typing import List
from functools import reduce

class Solution:
    def findSubstring_1(self, s: str, words: List[str]) -> List[int]:
        """
        我的算法1：时间复杂度为O(NK)(N为s的长度，K为words的长度)
        思想：遍历s，判断以此字符开头长度为words字符总长(因为words元素长度一致，可以设步长为words元素长度)的字符是否符合要求
        结果：LeetCode超时
        """
        if not len(words):
            return []
        cache = set()
        for word in words:
            n = 1
            while (word, n) in cache:
                n += 1
            cache.add((word, n))
        buffer = set()
        sLen = len(s)
        wLen = len(words[0])
        wsLen = len(words)
        wsumLen = wLen * wsLen
        results = []
        for i in range(len(s) - wsumLen + 1):
            for j in range(i, sLen, wLen):
                subS = s[j: j+wLen]
                n = 1
                while (subS, n) in buffer:
                    n += 1
                if (subS, n) in cache:
                    buffer.add((subS, n))
                else:
                    buffer.clear()
                    break
                if len(buffer) == wsLen:
                    results.append(i)
                    buffer.clear()
                    break
        return results

    def findSubstring_2(self, s: str, words: List[str]) -> List[int]:
        """
        我的算法2：时间复杂度为O(MK)(M为s中符合要求的子串个数，K为words的长度)
        思想：从s中找出所有属于words的子串，然后再判断每个符合的子串是否有对应后续元素使其符合要求
        结果：LeetCode超时
        """
        if not len(words):
            return []
        results = []
        cache = set(words)
        buffer = {}
        wordBuffer = set()
        for word in words:
            n = 1
            while (word, n) in wordBuffer:
                n += 1
            wordBuffer.add((word, n))
        wLen = len(word)
        wsLen = len(words)
        wsumLen = wLen * wsLen
        for i in range(len(s) - wLen + 1):
            subS = s[i: i+wLen]
            if subS in cache:
                buffer[i] = subS
        for k in buffer:
            jump = False
            tmpBuffer = set()
            for i in range(k, wsumLen+k, wLen):
                subS = None
                if i in buffer:
                    subS = buffer[i]
                else:
                    jump = True
                    break
                n = 1
                while (subS, n) in tmpBuffer:
                    n += 1
                if (subS, n) in wordBuffer:
                    tmpBuffer.add((subS, n))
                else:
                    jump = True
                    break
            if jump:
                continue
            results.append(k)
        return results

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        leetcode-cn.com/u/powcai的算法：时间复杂度为O(N)(N为s的长度)
        思想：设words元素的长度为wlen，以wlen步长遍历s，探索符合要求的子串，此步循环wlen次
        """
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:return []
        words = Counter(words)
        res = []
        # 遍历wlen次
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            # 探索符合要求的子串
            # 由left和rigth构建成一个探索窗口，将不可能是符合要求的子串的子串排除出去，
            # 当窗口的长度为符合要求的子串的长度时，探索成功，将头索引放入结果集
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                # 如果后一个单词不属于words，则直到此单词为止的子串一定不是符合要求的子串，放弃，继续向后探索
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                # 如果后一个单词属于words
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    # 如果后一单词是多余的重复元素，则窗口右移以排除掉最前面被重复的元素
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res


class Test(TestCase):
    def setUp(self):
        self.s = "wordgoodgoodgoodbestword"
        self.words = ["word","good","best","good"]
        self.sol = Solution()

    def test_sol1(self):
        result = self.sol.findSubstring_1(self.s, self.words)
        self.assertEqual(result, [8])

    def test_sol2(self):
        result = self.sol.findSubstring_2(self.s, self.words)
        self.assertEqual(result, [8])

    def test_sol(self):
        result = self.sol.findSubstring(self.s, self.words)
        self.assertEqual(result, [8])

if __name__ == '__main__':
    main()
