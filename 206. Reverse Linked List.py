# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # 迴圈寫法
    def reverseList_while(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 最開始時，prev 指向 None
        curr = head  # curr 指向鏈表的頭部

        while curr:
            next_temp = curr.next  # 暫存當前節點的下一個節點
            curr.next = prev  # 將當前節點的 next 指向前一個節點
            prev = curr  # prev 向前移動到當前節點
            curr = next_temp  # curr 向前移動到下一個節點

        return prev  # 最終 prev 會指向新的頭節點

    # 遞迴
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 基本情況：如果到達鏈表尾部，返回新的頭節點
        if not head or not head.next:
            return head

        # 遞歸反轉餘下的鏈表
        new_head = self.reverseList(head.next)

        # 將當前節點的 next（原來的下一個節點）的 next 指向當前節點
        head.next.next = head
        # 切斷當前節點的 next，防止形成環
        head.next = None

        return new_head
