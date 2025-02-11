"""
「Hard」題目來源：blind-75-leetcode-questions

23. Merge k Sorted Lists


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
"""
2025/2/11
暴力解 Time Limit Exceeded：使用 Merge 2 Sorted Lists 遞迴解法 再加一個迴圈解。O(N × log K)

使用heapq方法，把所有值丟到heapq裡面，每次以最小值拼接。O(N × K)

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 暴力解
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        def merge2Lists(l1: ListNode, l2: ListNode):
            if not l1:
                return l2
            if not l2:
                return l1

            if l1.val < l2.val:
                l1.next = merge2Lists(l1.next, l2)
                return l1
            else:
                l2.next = merge2Lists(l1, l2.next)
                return l2


        for i in range(len(lists) - 1):
            lists[1] = merge2Lists(lists[0], lists[1])
            lists.pop(0)

        return lists[0]

import heapq

# heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        # 建立一個最小堆
        heap = []

        # 1. 先把每條鏈結串列的頭節點放入 heap 中
        #    heapq 需要 (值, 索引, 節點) 格式來排序並避免比較 ListNode 物件
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # 虛擬頭節點 (dummy)，方便拼接
        dummy = ListNode(0)
        current = dummy

        # 2. 不斷從 heap 中彈出最小值的節點
        while heap:
            val, idx, node = heapq.heappop(heap)
            # 將彈出的節點接到合併後串列
            current.next = node
            current = current.next
            # 若該節點還有後續，繼續放入堆中
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next












