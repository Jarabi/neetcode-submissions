class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

        # If index is out of bounds
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        # Create new node
        new_node = Node(val)

        # Check if head node present. If not -> new node
        if not self.head:
            self.head = new_node
            return

        # Traverse list until node->None. Insert new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, index: int) -> bool:
        current = self.head
        current_index = 0

        # If index is head, move pointer to current.next. Remove current
        if current and current_index == index:
            self.head = current.next
            current = None
            return True

        # Traverse the list to find index.
        prev = None
        while current and current_index != index:
            prev = current
            current = current.next
            current_index += 1
        
        if not current:
            return False
        
        # Remove found node
        prev.next = current.next
        current = None

        return True

    def getValues(self) -> List[int]:
        current = self.head
        values = []

        while current:
            values.append(current.data)
            current = current.next
        
        return values
        
