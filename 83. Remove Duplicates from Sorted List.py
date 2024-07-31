class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head

        while curr:
            runner = curr.next
            while runner and curr.val == runner.val:
                runner = runner.next
            curr.next = runner
            curr = runner
        return head
