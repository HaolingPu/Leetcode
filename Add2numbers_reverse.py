# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1,  l2):
        r1 =  self.reverse(l1)
        r2 =  self.reverse(l2)


        ans = None
        total = 0
        carry = 0
        while r1 or r2 or carry:
            val1 = r1.val if r1 else 0
            val2 = r2.val if r2 else 0
            total = val1 + val2 + carry
            newhead = ListNode(total % 10)
            carry = total // 10
            newhead.next = ans
            ans = newhead
            if r1:
                r1 = r1.next
            if r2:
                r2 = r2.next
        self.printl(ans)
        
        return ans

        
    def reverse(self, head):
        if not head:
            return None
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    
    def printl(self,  head):
        cur = head
        output = []
        while cur:
            output.append(str(cur.val))
            cur = cur.next

        print("->".join(output))


def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

sol = Solution()

# ✅ Example 1: [7,2,4,3] + [5,6,4] = [7,8,0,7]
l1 = build_list([7,2,4,3])
l2 = build_list([5,6,4])
print("Test 1:")
print("Input:")
print("l1 =", l1)
print("l2 =", l2)
print("Output:", sol.addTwoNumbers(l1, l2))
print("-" * 30)


l1 = build_list([5])
l2 = build_list([5])
print("Test 2:")
print("Input:")
print("l1 =", l1)
print("l2 =", l2)
print("Output:", sol.addTwoNumbers(l1, l2))
print("-" * 30)