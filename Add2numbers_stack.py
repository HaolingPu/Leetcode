# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        cur = self
        while cur:
            vals.append(str(cur.val))
            cur = cur.next
        return "->".join(vals)


def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []

        # Step 1: push all digits into stacks
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        # Step 2: add from the least significant digit
        while s1 or s2 or carry:
            val1 = s1.pop() if s1 else 0
            val2 = s2.pop() if s2 else 0
            total = val1 + val2 + carry
            carry = total // 10

            # Create new node at front
            node = ListNode(total % 10)
            node.next = head
            head = node

        return head
