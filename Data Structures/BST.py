class BST:

    def __init__(self, data, left=None, right=None):
        """
        :param data: data of the node
        :param left: node on the left (< data of node)
        :param right: node on the right (> data of the node)
        """
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"|{self.data}|"

    def insert(self, key):
        if key < self.data:
            if self.left is None:
                self.left = BST(key)
            else:
                self.left.insert(key)
        if key > self.data:
            if self.right is None:
                self.right = BST(key)
            else:
                self.right.insert(key)

    def in_order_traversal(self, func):
        if self.left is not None:
            self.left.in_order_traversal(func)

        func(self)

        if self.right is not None:
            self.right.in_order_traversal(func)

    def search(self, key):
        if self is not None:
            if key == self.data:
                return True, self.data

            else:
                if key < self.data:
                    if self.left is not None:
                        self.left.search(key)
                    else:
                        return False, None
                if key > self.data:
                    if self.right is not None:
                        self.right.search(key)
                    else:
                        return False, None

        return False, None

"""
TESTING
"""

def print_node(item):
    print(f"{item}")

namelist = ["Andrew", "Dennis", "Ben", "Emma", "Teus", "Julio", "Felice", "Bob"]
my_bst = BST("Rodd")
for name in namelist:
    my_bst.insert(name)

my_bst.in_order_traversal(print)

check_names = ["Andrew", "Dennis", "Ben", "Emma", "Teus", "James", "Julio", "Felice", "Bob"]
for name in check_names:
    stat, node = my_bst.search(name)
    if stat:
        print(f"Node found here: {node}")
    else:
        print(f"Node {name} is not in bst")