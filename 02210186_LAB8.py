RED = True
BLACK = False

class RBNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, color=BLACK)
        self.root = self.NIL

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = RED
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._left_rotate(node.parent.parent)
        self.root.color = BLACK

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
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

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node == self.NIL or node.key == key:
            return node != self.NIL
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def get_black_height(self):
        return self._get_black_height(self.root)

    def _get_black_height(self, node):
        height = 0
        while node != self.NIL:
            if node.color == BLACK:
                height += 1
            node = node.left
        return height

    def delete(self, key):
        print("Delete operation not implemented in this version.")

# ---------------------------------------
# ASCII-safe Print Function for Windows
# ---------------------------------------
def print_rb_tree(node, indent="", last=True, NIL=None):
    if node != NIL:
        print(indent, end="")
        if last:
            print("`-- ", end="")
            indent += "    "
        else:
            print("|-- ", end="")
            indent += "|   "

        color = "[R]" if node.color == RED else "[B]"
        print(f"{node.key} {color}")
        print_rb_tree(node.left, indent, False, NIL)
        print_rb_tree(node.right, indent, True, NIL)

# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    rb_tree.insert(10)
    rb_tree.insert(20)
    rb_tree.insert(30)
    rb_tree.insert(15)
    rb_tree.insert(25)

    print("Search 20:", rb_tree.search(20))  # True
    print("Search 99:", rb_tree.search(99))  # False
    print("Black Height:", rb_tree.get_black_height())

    print("\nRed-Black Tree Structure:")
    print_rb_tree(rb_tree.root, NIL=rb_tree.NIL)
