"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
给定的 n 保证是有效的。
尝试使用一趟扫描实现
"""

from unittest import TestCase, main

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cache = head
        tmp = head
        size = 0
        flag = False
        while tmp:
            tmp = tmp.next
            size += 1
            if flag:
                cache = cache.next
            else:
                flag = size > n
        if flag:
            cache.next = cache.next.next
            return head
        else:
            return head.next

class Test(TestCase):
    def test(self):
        x = ListNode(1)
        head = x
        for i in range(2, 6):
            x.next = ListNode(i)
            x = x.next
        sol = Solution()
        result = sol.removeNthFromEnd(head, 2)
        rStr = ''
        while result:
            rStr = '%s%d' % (rStr, result.val)
            result = result.next
        self.assertEqual(rStr, '1235')

if __name__ == '__main__':
    main()
