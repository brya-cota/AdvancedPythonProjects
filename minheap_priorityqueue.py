'''
This project implements an array-based heap from scratch. We then implement a priority queue from said heap.
A driver method is also demonstrated to ensure the heap and priority queue work.
'''

class MinHeap:
    # Initializing class. Stores elements in a list heap[] (array)
    def __init__(self):
        self.heap = []

    # Adds an element to the end of the list and then bubbles up the newly added element from the last index
    def add(self, element):
        self.heap.append(element)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, i):
        # Move element at index i UP until heap property holds
        # Cost = distance to the root in the worst case = O(log n)
        while i > 0:
            parent_index = (i - 1) // 2
            if self.heap[i] < self.heap[parent_index]:
                # Swap values if i is < parent_index
                self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]
                i = parent_index
            else:
                break

    def sift_down(self, i):
        # Move element at index i DOWN until heap property holds
        # Cost = the nodes HEIGHT, not the height of the whole tree
        while True:
            # Calculate the indices of the left and right children
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            # Swapping i (current element) with the smaller of it's two children
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def find_min(self):
        # Check if heap is empty
        if self.is_empty():
            return 0
        else:
            # The root is always the min value in a min-heap. Return the min value (root)
            return self.heap[0]

    def remove_min(self):
        # Check if heap is empty
        if self.is_empty():
            return 0
        # Save the min value (root) inside a variable to use later
        minimum_value = self.heap[0]
        # Pop the last value in the list, save it into variable last
        last = self.heap.pop()
        # Check that the heap still has elements
        if len(self.heap) > 0:
            # Move the popped element to the root
            self.heap[0] = last
            # Restore heap order
            self.sift_down(0)
        # Return the minimum value that was removed
        return minimum_value

    # Checks if heap is empty and returns 0 if it is
    def is_empty(self):
        return len(self.heap) == 0

    # Returns the size (length) of the heap
    def size(self):
        return len(self.heap)

    # Removes all elements from the heap
    def clear(self):
        self.heap = []
        return self.heap

    # Prints current state of the heap
    def print_heap(self):
        print(str(self.heap))

class PrioritizedItem: # Wrapper class

    next_order = 0     # Static field shared across all instances - to track arrival order

    def __init__(self, priority, element):
        # Creates a new PrioritizedItem with the specified data
        self.priority = priority
        self.element = element
        # Current arrival order
        self.arrival_order = PrioritizedItem.next_order
        # Increment the static tracker
        PrioritizedItem.next_order += 1

    # Magic "dunder" method -- less than
    def __lt__(self, next_priority):
        if self.priority != next_priority.priority:
            # Lower value means higher priority
            return self.priority < next_priority.priority
        # If same priority, first come, first served
        return self.arrival_order < next_priority.arrival_order

    def __str__(self):
        return f"{self.priority}, {self.element}"

class PriorityQueue:
    def __init__(self):
        # Creates an empty priority queue
        self.heap = MinHeap()

    # Adds the given element to our PriorityQueue
    def enqueue(self, obj, priority):
        added_item = PrioritizedItem(priority, obj)
        self.heap.add(added_item)

    # Removes and returns the highest priority element (the smallest value in a min heap)
    def dequeue(self):
        removed_item = self.heap.remove_min()
        return removed_item

    # Peek (find min) at the highest priority element
    def peek(self):
        peeked_item = self.heap.find_min()
        return peeked_item

    def is_empty(self):
        return self.heap.is_empty()

    def size(self):
        return self.heap.size()

    def clear(self):
        self.heap.clear()

# Driver method - demonstrates how both heap and priority queue work
def main():
    # Instance of min-heap class object
    my_heap = MinHeap()

    # 15 integers to input into the heap
    my_heap_list = [2,7,45,67,77,9,0,43,10,58,12,15,56,11,7]

    # Iterate over each integer in the list and add it to my_heap instance
    for item in my_heap_list:
          my_heap.add(item)

    print("\nHeap Demo\n---------------------------")
    print("Original heap:")
    my_heap.print_heap()
    print(f"Current heap size: {my_heap.size()} ")
    print(f"Minimum item in the heap: {my_heap.find_min()}")
    print(f"Removing minimum item: {my_heap.remove_min()}")
    print("Sorted heap (with new min at root):")
    my_heap.print_heap()

    print("\nPriority Queue Demo\n---------------------------")
    # Instance of priority queue class object
    pq = PriorityQueue()
    pq.enqueue("Zoe", 1)
    pq.enqueue("Roxy", 7)
    pq.enqueue("Matt", 0)
    pq.enqueue("Ramon",200)
    pq.enqueue("Aria", 99)
    pq.enqueue("Jerrica", 10)
    pq.enqueue("Teena", 7)
    pq.enqueue("Jayme", 15)
    pq.enqueue("Travis", 22)
    pq.enqueue("Lupita", 35)
    pq.enqueue("Kayla", 87)
    pq.enqueue("Kenzie", 91)
    pq.enqueue("Lily", 46)
    pq.enqueue("Deon", 30)
    pq.enqueue("Chris", 62)

    while not pq.is_empty():
        print(pq.dequeue())

    print(f"Highest priority item: {pq.peek()}")

if __name__ == "__main__":
    main()
