#Part 1: Queue Implementation using Array
#Task 1: Implement the arrayQueue Class Structure

class ArrayQueue:
    def __init__ (self, capacity=10):
        self.capacity= capacity
        self.queue = [None]*capacity
        self.front= -1
        self.rear= -1
        print (f"Created new Queue with capacity: {capacity}")
    
    def is_empty(self):
        return self.front== -1
    
queue = ArrayQueue()
print(f"Queue is empty: {queue.is_empty()}")

#Task 2: Implement Array-based Queue Operations

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        removed_element = self.queue.pop(0)
        print(f"Dequeued element: {removed_element}")
        return removed_element

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def display(self):
        print(f"Display queue: {self.queue}")

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()

queue.enqueue(10)
queue.display()  

queue.enqueue(20)
queue.display()  

queue.enqueue(30)
queue.display()  

print(f"Front element: {queue.peek()}")  

queue.dequeue()  
queue.display()  

print(f"Queue size: {queue.size()}") 

