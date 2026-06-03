class DynamicArray:
    """
    A custom implementation of a dynamic array (resizable array) using a 
    fixed-size list simulation under the hood.
    """
    def __init__(self, capacity: int):
        """
        Initializes an empty dynamic array with a fixed initial capacity.
        
        :param capacity: The initial maximum number of elements the array can hold before resizing.
        """
        self.capacity = capacity
        self.size = 0
        # Pre-allocate memory by defining an empty array with the defined capacity
        self.arr = [None] * self.capacity

    def get(self, i: int) -> int:
        """
        Returns the element at the specified index. Assumes index i is valid.
        
        :param i: The target index.
        :return: The integer value at index i.
        """
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        """
        Overwrites the element at the specified index with a new value. Assumes index i is valid.
        
        :param i: The target index.
        :param n: The new integer value to insert.
        """
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        """
        Appends an element to the end of the array. 
        Automatically doubles the capacity if the array is full.
        
        :param n: The integer element to append.
        """
        # If the array is full, double the capacity before inserting
        if self.size == self.capacity:
            self.resize()
        
        # Insert element into the next available index and increment size
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        """
        Removes and returns the element at the end of the array.
        Assumes the array is non-empty.
        
        :return: The popped integer element.
        """
        # Retrieve the element at the logical end of the array
        popped_element = self.arr[self.size - 1]

        # Clean up the reference to prevent memory leaks, then update the size
        self.arr[self.size - 1] = None
        self.size -= 1

        return popped_element
 
    def resize(self) -> None:
        """
        Doubles the internal capacity of the array.
        
        Optimized to extend the existing list in-place rather than allocating 
        a brand new list and copying elements manually.
        """
        # In-place extension reduces overhead compared to manual loop copying
        self.arr.extend([None] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        """
        Returns the total number of elements currently stored in the array.
        
        :return: Logical size of the array.
        """
        return self.size

    def getCapacity(self) -> int:
        """
        Returns the current maximum capacity of the underlying array allocation.
        
        :return: Total memory capacity currently allocated.
        """
        return self.capacity
