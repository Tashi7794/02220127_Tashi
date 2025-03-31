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
