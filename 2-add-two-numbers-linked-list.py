from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_to_listnode(n_list):
    if len(n_list) == 0:
        return None

    head = ListNode(n_list[0])
    current = head

    for i in range(1, len(n_list)):
        current.next = ListNode(n_list[i])
        current = current.next

    return head


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        current = head

        while l1 is not None or l2 is not None:
            sum_ = carry

            if l1 is not None:
                sum_ += l1.val
                l1 = l1.next

            if l2 is not None:
                sum_ += l2.val
                l2 = l2.next

            carry = sum_ // 10
            current.next = ListNode(sum_ % 10)
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return head.next



solution = Solution()
n_1 = convert_list_to_listnode([1, 2, 3])
n_2 = convert_list_to_listnode([4, 5, 6])
print(solution.addTwoNumbers(n_1, n_2))
