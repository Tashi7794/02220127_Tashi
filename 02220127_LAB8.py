class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def search(self, key):
        return self._search(self.root, key)

    def get_height(self):
        return self._get_height(self.root)

    def is_balanced(self):
        return self._is_balanced(self.root)

    def print_tree(self):
        self._print_tree(self.root, "", True)

    def _print_tree(self, node, indent, last):
        if node:
            print(indent, "`- " if last else "|- ", node.key, sep="")
            indent += "   " if last else "|  "
            self._print_tree(node.left, indent, False)
            self._print_tree(node.right, indent, True)

    # Helper functions
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Balance cases
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root)
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root)
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _search(self, node, key):
        if not node or node.key == key:
            return node is not None
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _is_balanced(self, node):
        if node is None:
            return True
        lh = self._get_height(node.left)
        rh = self._get_height(node.right)
        if abs(lh - rh) > 1:
            return False
        return self._is_balanced(node.left) and self._is_balanced(node.right)

# -------------------------
# Testing the AVL Tree
# -------------------------
if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)

    print("Is Balanced:", avl_tree.is_balanced())  # True
    print("Tree Height:", avl_tree.get_height())   # Should return correct height
    print("Search 20:", avl_tree.search(20))       # True
    print("Search 99:", avl_tree.search(99))       # False

    print("\nAVL Tree Structure:")
    avl_tree.print_tree()

    avl_tree.delete(30)
    print("\nDeleted 30")
    print("Is Balanced after deletion:", avl_tree.is_balanced())
    print("Search 30:", avl_tree.search(30))       # False

    print("\nAVL Tree Structure After Deletion:")
    avl_tree.print_tree()
