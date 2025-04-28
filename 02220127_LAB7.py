#Task 1: Implementthe Node and Binary Tree Class Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
            print("Created new Binary Tree")
            print(f"Root: {self.root.value}")
        else:
            self.root = None
            print("Created new Binary Tree")
            print("Root: None")

# Example usage:
if __name__ == "__main__":
    # Create an empty binary tree
    tree1 = BinaryTree()


#Task 2: Implement Tree Information Methods
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_complete_binary_tree(self, node, index, number_of_nodes):
        if node is None:
            return True
        if index >= number_of_nodes:
            return False
        return (self.is_complete_binary_tree(node.left, 2 * index + 1, number_of_nodes) and
                self.is_complete_binary_tree(node.right, 2 * index + 2, number_of_nodes))

    def get_height(self):
        return self.height(self.root)

    def get_size(self):
        return self.size(self.root)

    def get_leaf_count(self):
        return self.count_leaves(self.root)

    def get_full_binary_check(self):
        return self.is_full_binary_tree(self.root)

    def get_complete_binary_check(self):
        total_nodes = self.size(self.root)
        return self.is_complete_binary_tree(self.root, 0, total_nodes)

# Example Usage
bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

print(f"Tree Height: {bt.get_height()}")
print(f"Total Nodes: {bt.get_size()}")
print(f"Leaf Nodes Count: {bt.get_leaf_count()}")
print(f"Is Full Binary Tree: {bt.get_full_binary_check()}")
print(f"Is Complete Binary Tree: {bt.get_complete_binary_check()}")
