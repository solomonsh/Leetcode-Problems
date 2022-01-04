# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head):
        # if head node is None return None
        if head is None:
            return None

        # Previous will keep track of previous nodes, current would keep track of the current nodes
        previous = None
        current = head

        # Loop through the linked list
        while current:
            # Save current's next on next variable, set the next of the current variable to previous and set previous to current
            next = current.next
            current.next = previous
            previous = current

            # If the loop is on the last item, set head to the last element of the linkedlist
            if next is None:
                head = current
            current = next
        return head

# To loop through a linked list and print it's values


def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next


list1 = [1, 2, 3, 4, 5]
head = ListNode(list1[0])
current = head

for l in range(1, len(list1)):
    current.next = ListNode(list1[l])
    current = current.next

sol = Solution()
head1 = None
print_linked_list(sol.reverseList(head))
