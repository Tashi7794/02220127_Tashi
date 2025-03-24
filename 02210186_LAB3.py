# Task 1 Stack Impementation Using Array
class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * capacity  
        self.top = -1  
        
        print(f"Created new ArrayStack with capacity: {self.capacity}")

    def is_empty(self):
        return self.top == -1


stack = ArrayStack()  
print(f"Stack is empty: {stack.is_empty()}")

#Task 2 Implement Array-based stack Operations

class ArrayStack:
    def __init__(self, capacity=10):
    
        self.capacity = capacity
        self.stack = [None] * capacity  
        self.top = -1 
        
        print(f"Created new ArrayStack with capacity: {self.capacity}")

    def is_empty(self):
        return self.top == -1

    def push(self, element):
        if self.top < self.capacity - 1:
            self.top += 1
            self.stack[self.top] = element
            print(f"Pushed {element} to the stack")
        else:
            print("Stack is full, cannot push element.")

    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[self.top]
            self.top -= 1
            print(f"Popped element: {popped_element}")
            return popped_element
        else:
            print("Stack is empty, cannot pop element.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            print("Stack is empty, no top element.")
            return None

    def size(self):
        return self.top + 1

    def display(self):
        if not self.is_empty():
            print(f"Display stack: {self.stack[:self.top+1]}")
        else:
            print("Stack is empty.")


stack = ArrayStack()  
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()


top_element = stack.peek()
print(f"Top element: {top_element}")

stack.pop()

stack_size = stack.size()
print(f"Stack size: {stack_size}")

stack.display()
