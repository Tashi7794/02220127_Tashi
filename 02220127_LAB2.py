#Task 1
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0  

    def __str__(self):
        if self.head is None:
            return "Created new LinkedList\nCurrent size: 0\nHead: None"
        else:
            return f"Created new LinkedList\nCurrent size: {self.size}\nHead: {self.head.data}"
            
my_list = LinkedList()
print(my_list)


#Task 2
class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self._size = 0  

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1  
        print(f"Appended {element} to the list")

    def get(self, index):
        if 0 <= index < self._size:
            current = self.head
            for _ in range(index):
                current = current.next
            print(f"Element at index {index}: {current.data}")
            return current.data
        else:
            print("Index out of bounds")
            return None  

    def set(self, index, element):
        if 0 <= index < self._size: 
            current = self.head
            for _ in range(index):
                current = current.next
            current.data = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Index out of bounds")

    def size(self):
        print(f"Current size: {self._size}")  
        return self._size

    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self._size += 1 
        print(f"Prepended {element} to the list")

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"Print Linked list: [{' '.join(elements)}]")


my_list = LinkedList()
my_list.append(5)
my_list.get(0)
my_list.set(0, 10)
my_list.get(0)
my_list.size()  
my_list.prepend(1)
my_list.print_list()