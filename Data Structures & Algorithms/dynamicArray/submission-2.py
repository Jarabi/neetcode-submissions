class DynamicArray:
    
    def __init__(self, capacity: int):
        # Define the size and capacity of the array
        self.capacity = capacity
        self.size = 0

        # Define empty array with defined capacity
        self.arr = [None] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        # First, check if array is full
        if self.size == self.capacity:
            # If full resize
            self.resize()
        
        # Insert element to the end of array
        self.arr[self.size] = n

        # Increase size of array
        self.size += 1


    def popback(self) -> int:
        # Get the element at the end of the array
        popped_element = self.arr[self.size - 1]

        # Clean up reference to the last element
        self.arr[self.size - 1] = None

        # Update array size
        self.size -= 1

        # Return popped element
        return popped_element
 

    def resize(self) -> None:
        # Extend the array
        self.arr.extend([None] * self.capacity)
        
        # Double the capacity
        self.capacity *= 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
