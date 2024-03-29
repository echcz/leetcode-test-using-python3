"""
给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
"""

from unittest import TestCase, main

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        js = set(J)
        result = 0
        for s in S:
            if s in js:
                result += 1
        return result

class Test(TestCase):
    def test(self):
        J = 'aA'
        S = 'aAAbbbb'
        sol = Solution()
        result = sol.numJewelsInStones(J, S)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    main()
