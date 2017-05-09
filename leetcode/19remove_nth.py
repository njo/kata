#  https://leetcode.com/problems/remove-nth-node-from-end-of-list/#/description


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = head
        progressed = 0
        nback = head

        while tail.next is not None:
            tail = tail.next
            progressed += 1
            if progressed > n:
                nback = nback.next

        nback.next = nback.next.next

        return head


def print_ll(ll):
    while ll is not None:
        print ll.val,
        ll = ll.next
        if ll is not None:
            print '->',
    print ""


def build_ll(l):
    head = ListNode(l[0])
    tail = head
    for x in l[1:]:
        this = ListNode(x)
        tail.next = this
        tail = this
    return head

head = build_ll(range(2))
print_ll(head)
print_ll(Solution().removeNthFromEnd(head, 2))
