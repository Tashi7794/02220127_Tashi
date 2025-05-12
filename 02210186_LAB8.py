#Part 2 Red-Black Tree Implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.color = 'red'  # New nodes are always red initially
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)  # NIL node, used for leaves
        self.TNULL.color = 'black'  # NIL nodes are always black
        self.root = self.TNULL

    # Left Rotate
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Right Rotate
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Fix the Red-Black Tree properties after insertion
    def fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    # Insert a new node with the given value
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.value = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 'black'
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    # Search for a node with a given value
    def search_tree(self, node, key):
        if node == self.TNULL or key == node.value:
            return node
        if key < node.value:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

    # Get the black height of the tree
    def get_black_height(self):
        return self._get_black_height(self.root)

    def _get_black_height(self, node):
        if node == self.TNULL:
            return 1
        left_height = self._get_black_height(node.left)
        right_height = self._get_black_height(node.right)
        if left_height != right_height:
            raise ValueError("Black height is not consistent!")
        return left_height + (1 if node.color == 'black' else 0)

    # In-order traversal for printing
    def inorder_helper(self, node):
        if node != self.TNULL:
            self.inorder_helper(node.left)
            print(node.value, end=" ")
            self.inorder_helper(node.right)

    # Public method to start inorder traversal
    def inorder(self):
        self.inorder_helper(self.root)
        print()

# Example usage:
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)

# In-order traversal
rb_tree.inorder()  # Should print the tree in sorted order

# Get black height
print(rb_tree.get_black_height())  # Returns the black height of the tree
