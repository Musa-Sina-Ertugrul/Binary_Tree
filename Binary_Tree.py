class BinarySeacrhTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySeacrhTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySeacrhTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        level = 0
        if self.data == val:
            return level
        if val < self.data:
            if self.left:
                print("left")
                return 1 + self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                print("right")
                return 1 + self.left.search(val)
            else:
                return False

    def find_max(self):
        if self.right:
            return self.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.find_min()
        else:
            return self.data

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left =self.left.delete(val)
            else:
                return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                return None
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    root = BinarySeacrhTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_tree = build_tree(numbers)
print(numbers_tree.in_order_traversal())
print(numbers_tree.search(1))
numbers_tree.delete(9)
print(numbers_tree.in_order_traversal())
numbers_tree.delete(20)
print(numbers_tree.in_order_traversal())
