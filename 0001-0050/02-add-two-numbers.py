
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        ls = []
        dummyHead = ListNode(0)
        dummyHead.next = self
        curr = dummyHead
        while curr.next is not None:
            ls.append(curr.next.val)
            curr = curr.next
        return '%s' % ls


class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:        
        if len(l1)< len(l2):
            temp = l1
            l1 = l2
            l2 = temp
        max_len = len(l1)
        for i in range(max_len):
            if i>=len(l2):
                return l1
            l1[i] = l1[i] + l2[i]
            if l1[i] >=10 :
                l1[i] = l1[i] % 10
                if i+1 < max_len:
                    l1[i+1] += 1
                else:
                    l1.append(1)
                    return l1
        return l1


    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        dummyHead = ListNode(0)
        curr = dummyHead
        p, q = l1, l2
        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = carry + x + y  
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p is not None :
                p = p.next 
            if q is not None :
                q = q.next          
        if carry > 0:
            curr.next = ListNode(1)
        return dummyHead.next


def list2ListNode(ls:list)->ListNode:
    lnDummyHead = ListNode(0)
    curr = lnDummyHead
    for i in range(len(ls)):
        curr.next = ListNode(ls[i])
        curr = curr.next
    return lnDummyHead.next
            
if __name__ == '__main__':
    l1 = [2,4,6]
    l2 = [5,6,4]
    ln1 = list2ListNode(l1)
    ln2 = list2ListNode(l2) 
    print(l1)
    print(l2)
    print(Solution().addTwoNumbers2(ln1,ln2))

