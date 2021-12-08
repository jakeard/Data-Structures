class BST:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self._insert(data, self.root)

    def _insert(self, data, curr_node):
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
                self._insert(data, curr_node.left)
        else:
            if curr_node.right is None: 
                curr_node.right = BST.Node(data)
            else:
                self._insert(data, curr_node.right)

    def traverse(self):
        for i in iter(bst):
            print(i)

    def __iter__(self):
        yield from self._yield_node_data(self.root)
    
    def _yield_node_data(self, curr_node):
        if curr_node is not None:
            yield from self._yield_node_data(curr_node.left) 
            yield curr_node.data 
            yield from self._yield_node_data(curr_node.right)
        


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
# TODO - Create a function in the BST class called "insert" that will insert a new node into the BST. 
# There should be no nodes with the same data value. If a duplicate node tries to be inserted, print 
# "Node already exists". Create any extra functions that you may need.

bst.insert(1)
print(bst.root.data) # 3
print(bst.root.left.data) # 1
bst.insert(5)
bst.insert(4)
bst.insert(3) # Node already exists
print(bst.root.right.data) # 5
print(bst.root.right.left.data) # 4


print('\n------------------------------')
print('EXERCISE 3')
print('------------------------------')
# TODO - Create a function in the BST class clled "traverse" to traverse through the BST and print all 
# nodes' data values. You may need to define the __iter__ function, which will iterate through the tree, 
# calling your traverse function and using the yield command to get the node data. Create any extra functions 
# that you may also need.

bst.insert(7)
bst.insert(6)
bst.insert(0)
bst.insert(-1)
bst.insert(11)
bst.insert(22)
bst.insert(-3)
bst.traverse() # Output: -3, -1, 0, 1, 3, 4, 5, 6, 7, 11, 22             