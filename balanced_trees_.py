'''
Brya Cota
This project is a self-balancing binary search tree built from the ground up and divided into 2 parts.
Part 1: Implement a Standard Binary Search Tree (BST) (50 points)
Part 2: Extend it to a Self-Balancing Tree (AVL)
'''

# Set up node attributes and initialize height to 0
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

# Standard BST/AVL class with the entry point of the tree and a counter to keep track of total nodes in O(1) time
class BinarySearchAVLTree:
    def __init__(self):
        self.root = None
        self.node_tracker = 0

    def insert(self, key, value):
        # Public entry point for inserting data starting at the root
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        # Base case: if we've past a leaf and in an empty slot. New node will be inserted
        if node is None:
            # Update node count
            print("Inserting: ", key)
            self.node_tracker += 1
            return Node(key, value)
        # Key is smaller than current node, goes to the left
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        # Key is larger than current node, goes to the right
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        # Key already exists - update the value placeholder WITHOUT changing size
        else:
            node.value = value
            return node

        # Restore AVL property
        return self.restore_balance(node)

    def search(self, key): # return value if found, null otherwise.
        # Public entry point for searching through the data starting at the root
        return self._search(self.root, key)

    def _search(self, node, key):
        # Base case: the key doesn't exist in the tree
        if node is None:
            return None
        # If key is at the root, return root value
        if key == node.key:
            return node.value
        # Otherwise search left
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):  # handle 0, 1, or 2 children cases using successor
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        #Base case
        if node is None:
            return None
        # Search left
        if key < node.key:
            node.left = self._delete(node.left, key)
        # Search right
        elif key > node.key:
            node.right = self._delete(node.right, key)
        # Node to delete is found, handle cases
        else:
            # No (0) children, leaf
            if node.left is None and node.right is None:
                self.node_tracker -= 1
                return None
            # One (1) child
            if node.left is None:
                self.node_tracker -= 1
                return node.right
            if node.right is None:
                self.node_tracker -= 1
                return node.left
            # Two (2) children - using successor since we have 2 pointers (prev and next)
            # Find inorder successor (smallest value greater than the node)
            successor = self._find_min(node.right)

            # Make a copy of the successors key and value into current node
            node.key = successor.key
            node.value = successor.value
            # Delete original successor key and value
            node.right = self._delete(node.right, successor.key)

        return self.restore_balance(node)

    # Helper method
    def _find_min(self, node):
        # Base Case
        # BST Properties: Min will be on the left. If no left child - we're already at the min node
        if node.left is None:
            return node
        else:
            # Keep searching until min is found
            return self._find_min(node.left)

    def height(self): #null/empty tree height can be -1 or 0
       return self._height(self.root)

    def _height(self, node):
        # Base Case
        if node is None:
            return -1
        return node.height

    def size(self):  #number of nodes in the tree
        return self.node_tracker

    def inorder_traversal(self): #print keys in sorted order (traverse left -> visit root -> traverse right) (or collect in a list).
        node_list = []
        self._inorder_traversal(self.root, node_list)
        return node_list

    def _inorder_traversal(self, node, node_list):
        # Base case
        if node is None:
            return
        # Visit left most node first, until None, append, back to root, then visit right subtree
        self._inorder_traversal(node.left, node_list)
        node_list.append((node.key, node.value))
        self._inorder_traversal(node.right, node_list)

        return

    def _update_height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)

        node.height = max(left_height, right_height) + 1
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)

        balance_factor = right_height - left_height
        return balance_factor

    def right_rotation(self, y): # Single right rotation (used when left subtree of left child is too heavy)
        # x is the left child of unbalanced node y
        x = y.left
        n = x.right

        x.right = y
        y.left = n

        self._update_height(y)
        self._update_height(x)
        # x is now the new root
        return x

    def left_rotation(self, x): # Single left rotation (used when right subtree of the right child is too heavy)
        # y is the right child of the unbalanced node x
        y = x.right
        n = y.left

        y.left = x
        x.right = n

        self._update_height(x)
        self._update_height(y)
        # y is now the new root
        return y

    # Perform rotations to restore balance; if |balance| > 1
    def restore_balance(self, node):
        self._update_height(node)
        balance_factor = self._get_balance(node)
        # LL - single right rotation (used when left subtree of left child is too heavy)
        if balance_factor < -1 and self._get_balance(node.left) <= 0:
            print("LL Rotation at: ", node.key)
            return self.right_rotation(node)
        # RR - single left rotation (used when right subtree of right child is too heavy)
        if balance_factor > 1 and self._get_balance(node.right) >= 0:
            print("RR Rotation at: ", node.key)
            return self.left_rotation(node)
        # LR - left rotation on left child then right rotation on unbal. node (used when left child is right-heavy)
        if balance_factor < -1 and self._get_balance(node.left) > 0:
            node.left = self.left_rotation(node.left)
            print("LR Rotation at: ", node.key)
            return self.right_rotation(node)
        # RL - right rotation on the right child then a left rotation on unbal. node (used when right child is left-heavy)
        if balance_factor > 1 and self._get_balance(node.right) < 0:
            node.right = self.right_rotation(node.right)
            print("RL Rotation at: ", node.key)
            return self.left_rotation(node)
        return node

def main():
    # Insert 15 elements
    tree = BinarySearchAVLTree()
    tree.insert(9, "A")
    tree.insert(3, "B")
    tree.insert(1, "C")
    tree.insert(14, "D")
    tree.insert(18, "E")
    tree.insert(30, "F")
    tree.insert(25, "G")
    tree.insert(67, "H")
    tree.insert(5, "I")
    tree.insert(7, "J")
    tree.insert(16, "K")
    tree.insert(11, "L")
    tree.insert(10, "M")
    tree.insert(44, "N")
    tree.insert(8, "O")
    #tree.print_to_string()

    # Demonstrating search() function
    print(f"\nSearch for 5: {tree.search(5)}")
    print(f"Search for 7: {tree.search(7)}")

    # Demonstrating inorder_traversal() function
    print(f"\nInorder traversal: {tree.inorder_traversal()}")

    # Demonstrating delete() function
    tree.delete(44)
    print(f"\nAfter deleting 44: {tree.inorder_traversal()}")

    # Demonstrating height() and size() functions
    print(f"\nHeight of tree: {tree.height()}")
    print(f"Size of tree: {tree.size()}")

if __name__ == "__main__":
    main()


