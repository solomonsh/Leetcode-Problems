class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
     # def hasCycle(self, head):
        
    #     unique_nodes = set()
    #     current = head
    #     while current:
    #         if current in unique_nodes:
    #             return True
    #         unique_nodes.add(current)
    #         current = current.next
           
    #     return False 

    def hasCycle(self, head):
        
        slow_pointer = head        
        fast_pointer = head

        while fast_pointer and slow_pointer:
       
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if fast_pointer is slow_pointer:
                return True
        
        return False

    
ls = [3,2,0,4]
root = ListNode(ls[0])
current = root
for l in range(1,len(ls)):
    current.next = ListNode(ls[l])
    current = current.next

current.next = root


s = root
# while s:
#     print(s.val)
#     s = s.next
    

sol  = Solution()
print(sol.hasCycle(root))

