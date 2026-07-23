# Assume you have an AVL node class defined below.
class RBNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.is_red = True  # New nodes in a Red-Black tree are typically inserted as Red

    # Write a method boolean isRed(node) that treats null (NIL) as black. Otherwise it's red
    def is_red(self, node):
        if node is None:
            return False

        return node.is_red

root = RBNode(10)

root.left = RBNode(5)
root.left.parent = root

root.right = RBNode(15)
root.right.parent = root

print(root.key)          # 10
print(root.left.key)     # 5
print(root.right.key)    # 15