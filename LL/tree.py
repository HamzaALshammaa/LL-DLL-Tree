class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.level = 0
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if self.value == value:
            return False
        elif self.value > value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
                return True

    def find(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            if self.left:
                return self.left.find(value)
            else:
                return False
        else:
            if self.right:
                return self.right.find(value)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value), end=' - ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value), end=' ')

    def eando(self):
        if self:
            if self.left is None and self.right is None:
                print(str(self.value), end=' - ')
                # print(" ----------------")
                if self.value % 2 == 0:
                    self.value = str(self.value)
                    self.value = 'E'
                else:
                    self.value = str(self.value)
                    self.value = 'O'
            # if self.left:
            #     self.left.eando()
            # if self.right:
            #     self.right.eando()
            # print(self.value)

    def inorder(self):
        if self:
            if self.left:
                self.left.postorder()
            print(str(self.value), end=' - ')
            if self.right:
                self.right.postorder()


class Tree:
    def __init__(self):
        self.root = None
        self.value = None

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def eando1(self):
        if self.root:
            if self.root.left:
                self.root.left.eando()
            if self.root.right:
                self.root.right.eando()
            # print(self.value)
            return self.root.eando
        # else:
        #     return False

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False

    def preorder(self):
        print('Preorder:')
        if self.root is None:
            print('this is empty')
        else:
            self.root.preorder()
        print(" ")

    def postorder(self):
        print('Postorder:')
        self.root.postorder()

    def inorder(self):
        print('Inorder:')
        self.root.inorder()

    def remove(self, key):
        node = self.root
        # find node to remove
        while node and node.value != key:
            parent = node
            if key < node.value:
                node = node.left
            elif key > node.value:
                node = node.right
        # case 1: value not found
        if node is None or node.value != key:
            print('The value is not found..!')
            return False
        # case 2: remove node has no children
        elif node.left is None and node.right is None:
            if key < parent.value:
                parent.left = None
            else:
                parent.right = None
        # case 3: remove node has left child only
        elif node.left and node.right is None:
            if key < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
        # case 4: remove node has right child only
        elif node.left is None and node.right:
            if key > parent.value:
                parent.right = node.right
            else:
                parent.left = node.left
        # case 5: remove has left and right children
        else:
            del_node_parent = node
            del_node = node.right
            new_root = self.root
            while del_node.left:
                del_node_parent = del_node
                del_node = del_node.left
            node.value = del_node.value
            if del_node.right:
                if del_node_parent.value > del_node.value:
                    del_node_parent.right = del_node.left
                else:
                    del_node_parent.right = del_node.right
            else:
                if del_node.value < del_node_parent.value:
                    del_node_parent.left = None
                else:
                    del_node_parent.right = None

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def diameter_of_binary_tree(self):
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.left)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)
        dfs(self.root)
        return res[0]


tree = Tree()
# s = int(input("enter Tree size: "))
# for Nodes in range(s):
#     tree.insert(input("enter the Node value: "))
tree.insert("A")
tree.insert("+")
tree.insert("B")
tree.insert("/")
tree.insert("C")
tree.insert("V")
tree.insert("-")
tree.insert("M")
tree.insert("*")
tree.insert("4")
# tree.insert(6)
# tree.insert(1)
# tree.insert(3)
# tree.insert(7)
# tree.insert(4)
# tree.insert(10)
tree.postorder()
print("-" * 20)
# tree.remove(input("enter the value you want to delete: "))
print('')
# tree.eando1()
# tree.preorder()
print("")
print("the height of the tree is: ", tree.height() - 1)
