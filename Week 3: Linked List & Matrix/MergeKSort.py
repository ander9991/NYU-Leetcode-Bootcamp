class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes=[]
        head = ListNode(0)
        point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
