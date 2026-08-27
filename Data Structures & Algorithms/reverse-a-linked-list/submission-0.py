# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def append(self,head,value):
        new_node = ListNode(value,None)
        if not head:
            head.val = new_node.value
            head.next = None
        else:
            while(head.next is not None):
                head=head.next
            head.next = new_node


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        if not head:
            return head
        else:
            arr=[]
            while(head.next is not None):
                arr.append(head.val)
                head=head.next
            for i in range(len(arr)-1,-1,-1):
                self.append(head,arr[i])
            
        return head
        