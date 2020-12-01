from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -\> List[int]:
        ans = []

        def loop(nums: List[int], node: ListNode):
            if node:
                loop(nums, node.next)
                nums.append(node.val)

        loop(ans, head)
        return ans
