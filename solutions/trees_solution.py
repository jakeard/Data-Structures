class BST:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
    
    def insert(self, data, curr_node):
        if self.root is None:
            self.root = BST.Node(data)
            return
        elif curr_node.data == data:
            print('Node already exists')
            return
        elif data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = BST.Node(data)
            else:
                self.insert(data, curr_node.left)
        else:
            if curr_node.right is None: 
                curr_node.right = BST.Node(data)
            else:
                self.insert(data, curr_node.right)


print('\n------------------------------')
print('EXERCISE 1')
print('------------------------------')
# TODO - Fill in the BST class and its inner Node class according to the data that we need 
# for a binary search tree. The following test cases should produce no errors.

bst = BST()
node = bst.Node(3)
bst.root = node


print('\n------------------------------')
print('EXERCISE 2')
print('------------------------------')
# TODO - Create a function in the BST class called insert that will insert a new node into the BST. 
# There should be no nodes with the same data value. If a duplicate node tries to be inserted, print 
# "Node already exists".

bst.insert(1, bst.root)
print(bst.root.data) # 3
print(bst.root.left.data) # 1
bst.insert(5, bst.root)
bst.insert(4, bst.root)
bst.insert(3, bst.root) # Node already exists
print(bst.root.right.data) # 5
print(bst.root.right.left.data) # 4


print('\n------------------------------')
print('EXERCISE 3')
print('------------------------------')