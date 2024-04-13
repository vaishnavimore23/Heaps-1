# TC = O(nlogk) -- n is avg length of linkedList
# sc = O(k)

from heapq import heapify, heappush, heappop
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Wrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

    def __eq__(self, other):
        return self.node.val == other.node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        heapify(heap)

        for head in lists:
            if head:
                heappush(heap, Wrapper(head))

        dummy = ListNode(-1)
        curr = dummy

        while heap:
            min_wrapper = heappop(heap)
            min_node = min_wrapper.node
            curr.next = min_node
            curr = curr.next
            if min_node.next:
                heappush(heap, Wrapper(min_node.next))

        return dummy.next
