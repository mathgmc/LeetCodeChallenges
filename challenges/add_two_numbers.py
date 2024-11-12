#https://leetcode.com/problems/add-two-numbers/description/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution0:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value = l1.val
        multiplier = 10
        
        while l1.next != None:
            l1 = l1.next
            l1_value += multiplier*l1.val
            multiplier *= 10

        l2_value = l2.val
        multiplier = 10
        
        while l2.next != None:
            l2 = l2.next
            l2_value += multiplier*l2.val
            multiplier *= 10

        total = l1_value + l2_value
        print(total)
        l3 = ListNode(total%10)
        print(f"total%10={total%10}")
        total = int(total/10)
        print(f"Novo Total: {total}")
        pointer = l3
        while total > 0:
            pointer.next = ListNode()
            pointer = pointer.next
            pointer.val = total%10
            print(f"total%10={total%10}")
            total = int(total/10)
            print(f"Novo Total: {total}")

        return l3


class Solution1: # Best solution
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rest = 0
        l3 = None
        val = l1.val + l2.val
        if val >= 10:
            val -= 10
            rest += 1

        l3 = ListNode(val)
        pointer_l3 = l3
        pointer_l1 = l1
        pointer_l2 = l2

        pointer_l1 = pointer_l1.next if pointer_l1 else None
        pointer_l2 = pointer_l2.next if pointer_l2 else None

        while pointer_l1 or pointer_l2: 
            val = rest
            rest = 0
            val += pointer_l1.val if pointer_l1 else 0
            val += pointer_l2.val if pointer_l2 else 0

            if val >= 10:
                val -= 10
                rest += 1

            pointer_l3.next = ListNode(val)
            pointer_l3 = pointer_l3.next

            pointer_l1 = pointer_l1.next if pointer_l1 else None
            pointer_l2 = pointer_l2.next if pointer_l2 else None

        if rest > 0:
            pointer_l3.next = ListNode(rest)
            pointer_l3 = pointer_l3.next
            
        return l3

