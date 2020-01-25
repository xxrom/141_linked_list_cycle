# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:

    def hasCycleSlow(self, head: ListNode) -> bool:
        memo = {}
        currentListNode = head

        if head == None:
            return False

        while memo.get(currentListNode) == None and currentListNode.next != None:
            memo[currentListNode] = True
            currentListNode = currentListNode.next

        return memo.get(currentListNode) == True

    def hasCycle(self, head: ListNode) -> bool:
        # at the beginning there are two runners
        # with different speed (X and 2X)
        # if there are will be cycle, they will meet each other
        tortoise = head  # X
        hare = head  # 2X

        while hare != None and hare.next != None and hare.next.next != None and tortoise != None and tortoise.next != None:
            hare = hare.next.next
            tortoise = tortoise.next

            if tortoise == hare:
                return True

        return False


my = Solution()

l0 = ListNode(3)
l1 = ListNode(2)
l2 = ListNode(0)
l3 = ListNode(-4)

l0.next = l1
l1.next = l2
l2.next = l3
l3.next = l1


print(my.hasCycle(l0))

# Runtime: 48 ms, faster than 63.86% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.

# Fast version
# Runtime: 40 ms, faster than 95.93% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
