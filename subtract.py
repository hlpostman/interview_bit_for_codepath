# subtract.py

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        """Modifies the values of the first half of the linked list passed by subtracting the value of the ith node of the second half of the linked list from the value of the ith node of the first half for nodes i = 0 to i = lenght//2.

            Args: A, the head node of a linked lists

            Returns: A, the head node of the linked list passed, where nodes 0 through length//2 have been modified

            Raises: TypeError - expecting linked list node
        """
        list_length = self.get_length(A)
        second_half_depth = list_length//2 if list_length%2 == 0 else list_length//2 + 1
        current_node_of_second_half = A # Initialize and then in next line advance
        for i in range(second_half_depth): # Advance to correct place
            current_node_of_second_half = current_node_of_second_half.next
        current_node_of_second_half = self.reverse_linked_list(current_node_of_second_half)
        current_node_of_first_half = A
        head_of_reversal = current_node_of_second_half

        # Loop through list in O(n)
        for i in range(list_length//2):
            # Update value
            current_node_of_first_half.val = current_node_of_second_half.val - current_node_of_first_half.val
            # Advance both pointers
            current_node_of_first_half = current_node_of_first_half.next
            current_node_of_second_half = current_node_of_second_half.next
        # Re-reverse second half in O(n)
        head_of_reversal = self.reverse_linked_list(head_of_reversal)
        return A

    def get_length(self, A):
    """Finds and returns the number of nodes in a linked list.  O(n) where n is the number of nodes after and including the head node passed.

    Args: A, the head of a linked list

    Returns: unsigned integer, the number of nodes after and including the head node A

    Raises:
        TypeError: A is not a node
    """
        length = 0
        current_node = A
        while current_node:
            length += 1
            current_node = current_node.next
        return length
    def reverse_linked_list(self, A):
    """Reverses the nodes of the linked list passed in place and returns the new head node.  O(n) where n is the number of nodes after and including the head node passed.

    Args: A, the head of a linked list

    Returns: A, the head of a linked list

    Raises:
        TypeError: A is not a node
    """
        prev = None
        current = A
        while current != None:
            next_node = current.next # Naturally!
            current.next = prev # Swap what was before and after current - i.e., reverse!
            prev = current # Advance for the next iteration
            current = next_node # Advance for the next iteration
        A = prev # Move A to what is now the head
        return A
