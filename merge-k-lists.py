"""
合并 k 个排序链表，返回合并后的排序链表。

注：此实现的时间复杂度为O(NlogK)(N为链表总结点数，K为链表数)
   使用简单/直接的方法(时间复杂度为O(NK))时，LeetCode超时
"""

from unittest import TestCase, main
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return lists
        step = 1
        length = len(lists)
        while step < length:
            for i in range(0, length, step+step):
                lists[i] = self._mergeListNode(lists[i], lists[i+step]) if i+step < length else lists[i]
            step += step
        return lists[0]

    def _mergeListNode(self, a: ListNode, b: ListNode) -> ListNode:
        result = ListNode(0)
        tmp = result
        while a and b:
            if a.val < b.val:
                tmp.next = a
                tmp = tmp.next
                a = a.next
            else:
                tmp.next = b
                tmp = tmp.next
                b = b.next
        while a:
            tmp.next = a
            tmp = tmp.next
            a = a.next
        while b:
            tmp.next = b
            tmp = tmp.next
            b = b.next
        return result.next

class Test(TestCase):
    def test(self):
        lists = []
        a = ListNode(1)
        lists.append(a)
        a.next = ListNode(3)
        a = a.next
        a.next = ListNode(5)
        b = ListNode(1)
        lists.append(b)
        b.next = ListNode(3)
        b = b.next
        b.next = ListNode(4)
        c = ListNode(2)
        lists.append(c)
        c.next = ListNode(6)
        sol = Solution()
        result = sol.mergeKLists(lists)
        rStr = ''
        while result:
            rStr = '%s%d' % (rStr, result.val)
            result = result.next
        self.assertEqual(rStr, '11233456')

if __name__ == '__main__':
    main()
