# Part 2: Stack Implementation using Linked List
# Task 3: Implementthe Node and LinkedStack Class Structure
class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None  

class LinkedStack:
    def __init__(self):
        self.top = None 
        self.size = 0   
        print("Created new LinkedStack")
    
    def is_empty(self):
        return self.size == 0
    
    def __str__(self):
        return f"Stack is empty: {self.is_empty()}"

stack = LinkedStack() 
print(stack) 

# # Task 4: Implement Linked List-based Stack Operations
class Node:
    def __init__(self, data, next_node=None):
        self.data, self.next = data, next_node

class LinkedStack:
    def __init__(self):
        self.top, self.size = None, 0

    def push(self, element):
        self.top, self.size = Node(element, self.top), self.size + 1
        print(f"Pushed {element} to the stack")
        self.display()

    def pop(self):
        if self.is_empty(): return None
        popped, self.top = self.top.data, self.top.next
        self.size -= 1
        return popped

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.size == 0

    def display(self):
        current, elements = self.top, []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"Display stack: [{', '.join(elements)}]")

    def display_current_stack(self):
        current, elements = self.top, []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Current stack: " + " -> ".join(elements) + " -> null")

# Example usage
stack = LinkedStack()
stack.push(10)
stack.push(20)
stack.push(30)

print(f"Top element: {stack.peek()}")
print(f"Popped element: {stack.pop()}")
stack.display_current_stack()
print(f"Stack size: {stack.size}")
