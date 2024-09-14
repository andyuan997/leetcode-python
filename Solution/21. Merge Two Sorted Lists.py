# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode)-> ListNode:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        """
        if not list1: return list2
        if not list2: return list1
        dummy_node = ListNode(None)
        curr = dummy_node

        while list1 and list2:
            list1_val = list1.val
            list2_val = list2.val
            if list1_val < list2_val:
                curr.next = ListNode(list1_val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2_val)
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2


        return dummy_node.next

# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
