#Task 1
class CustomList:
    def __init__(self, capacity=10):
        self._capacity = capacity  
        self._size = 0  

        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")

my_list = CustomList()



#Task 2
class CustomList:
    def __init__(self):
        self._array = []  

    def append(self, element):
        self._array.append(element)
        print(f"Appended {element} to the list")

    def get(self, index):
        if 0 <= index < len(self._array):
            print(f"Element at index {index}: {self._array[index]}")
            return self._array[index]
        print("Index out of bounds")

    def set(self, index, element):
        if 0 <= index < len(self._array):
            self._array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Index out of bounds")

    def size(self):
        print(f"Current size: {len(self._array)}")
        return len(self._array)

my_list = CustomList()
my_list.append(5)
my_list.get(0)
my_list.set(0, 10)
my_list.get(0)
my_list.size()
