class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        while head:
            if head in hashmap.keys():
                return head
            else:
                hashmap[head] = 1
            head = head.next
