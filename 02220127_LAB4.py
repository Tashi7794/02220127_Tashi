# Part 2: Queue implementation using Linked List
# Task 3: Implementthe Node and LinkedStack Class Structure
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedQueue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0     
        print("Created new LinkedQueue")

    def is_empty(self):
        return self.size == 0

# Example usage
def main():
    queue = LinkedQueue()
    print("Queue is empty:", queue.is_empty())

if __name__ == "__main__":
    main()


# Task 4: Implement Linked List-based Queue Operations


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        print(f"Dequeued element: {removed}")
        print("Current queue:", self.get_queue_string())
        return removed

    def peek(self):
        return None if self.is_empty() else self.front.data

    def display(self):
        elements = self.get_queue_list()
        print("Display queue:", elements)

    def get_queue_list(self):
        current, elements = self.front, []
        while current:
            elements.append(str(current.data))
            current = current.next
        return "[" + ",".join(elements) + "]"

    def get_queue_string(self):
        current, elements = self.front, []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> null"

# Example usage
queue = LinkedQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element:", queue.peek())
queue.dequeue()
print("Queue size:", queue.size)
