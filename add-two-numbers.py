"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头
"""

from unittest import TestCase, main

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        target = None
        targetNext = None
        num = 0
        while l1 or l2 or num:
            lNum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + num
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if lNum > 9:
                lNum = lNum - 10
                num = 1
            else:
                num = 0
            l = ListNode(lNum)
            if targetNext:
                targetNext.next = l
                targetNext = targetNext.next
            else:
                target = l
                targetNext = target
        return target

class Test(TestCase):
    def test(self):
        x = ListNode(2)
        l1 = x
        x.next = ListNode(4)
        x = x.next
        x.next = ListNode(3)
        y = ListNode(5)
        l2 = y
        y.next = ListNode(6)
        y = y.next
        y.next = ListNode(4)
        sol = Solution()
        target = sol.addTwoNumbers(l1, l2)
        result = ''
        while target:
            result = '%s%d' % (result, target.val)
            target = target.next
        self.assertEqual(result, '708')

if __name__ == '__main__':
    main()
