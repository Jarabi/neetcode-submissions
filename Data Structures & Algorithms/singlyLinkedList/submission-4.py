from typing import List

class Node:
    """
    Represents a single node in a singly linked list.
    """
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    """
    A class to represent a singly linked list with standard operations 
    such as retrieval, insertion, deletion, and visualization.
    """
    
    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None
    
    def get(self, index: int) -> int:
        """
        Retrieves the value of the node at the specified index.
        
        Time Complexity: O(n) where n is the index.
        
        :param index: The 0-indexed position of the node to retrieve.
        :return: The integer value of the node, or -1 if the index is out of bounds.
        """
        current = self.head
        current_index = 0

        # Traverse the list until we find the index or hit the end
        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

        # If index is out of bounds
        return -1

    def insertHead(self, val: int) -> None:
        """
        Inserts a new node with the given value at the very beginning of the list.
        
        Time Complexity: O(1)
        
        :param val: The integer value to insert.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        """
        Inserts a new node with the given value at the end of the list.
        
        Time Complexity: O(n) because we must traverse to the end.
        
        :param val: The integer value to insert.
        """
        new_node = Node(val)

        # Edge case: If the list is empty, make this node the head
        if not self.head:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next

        # Link the last node to the new node
        current.next = new_node

    def remove(self, index: int) -> bool:
        """
        Removes the node at the specified index from the list.
        
        Time Complexity: O(n) to find the node.
        
        :param index: The 0-indexed position of the node to remove.
        :return: True if the node was successfully removed, False if the index is out of bounds.
        """
        current = self.head
        current_index = 0

        # Edge case: If removing the head node
        if current and current_index == index:
            self.head = current.next
            current = None
            return True

        # Traverse the list to find the targeted index, keeping track of the previous node
        prev = None
        while current and current_index != index:
            prev = current
            current = current.next
            current_index += 1
        
        # If the index is out of bounds (current walked off the end of the list)
        if not current:
            return False
        
        # Unlink the current node from the list by skipping over it
        prev.next = current.next
        current = None

        return True

    def getValues(self) -> List[int]:
        """
        Converts the linked list structure into a standard Python list of values.
        
        Time Complexity: O(n)
        
        :return: A list containing all node data in sequential order.
        """
        current = self.head
        values = []

        # Walk through the entire list and collect data
        while current:
            values.append(current.data)
            current = current.next
        
        return values
        
