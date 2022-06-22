# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2-4
       1-1-3-4
        
        list1.next = list2
        '''
        
        if not list1:
            return list2 
        if not list2:
            return list1 
        
        dummy_head = ptr = ListNode(0)
        
        while list1 and list2:
            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next 
                
            else:
                ptr.next = list2
                list2 = list2.next
                
            ptr = ptr.next 
            
        if list1:
            ptr.next = list1
            ptr = ptr.next 
        else:
            ptr.next = list2
            ptr = ptr.next
            
       
        return dummy_head.next
            
        
            
                
        