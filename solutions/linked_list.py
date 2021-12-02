

# EXERCISE 1:
class LinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
    
    def back_new_node(self, data):
        new_node = LinkedList.Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node 
    
    def front_new_node(self, data):
        new_node = LinkedList.Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def remove_tail(self):
        if self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def remove_head(self):
        if self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next


print('\n------------------------------')
print('EXERCISE 1')
print('------------------------------')
# TODO - Fill in the LinkedList class and its inner Node class according to the data that we need 
# for a linked list. The following test cases should produce no errors.

ll = LinkedList()
node = ll.Node(3)
ll.head = node
ll.tail = node


print('\n------------------------------')
print('EXERCISE 2')
print('------------------------------')
# TODO - Create a function called 'back_new_node' that will add a new node to the back of the linked list.

ll = LinkedList()
ll.back_new_node(1)
print(ll.head.data) # 1
print(ll.tail.data) # 1
ll.back_new_node(2)
ll.back_new_node(3)
ll.back_new_node(4)
print(ll.head.data) # 1
print(ll.tail.data) # 4
print(ll.head.next.data) # 2
print(ll.tail.prev.data) # 3


print('\n------------------------------')
print('EXERCISE 3')
print('------------------------------')
# TODO - Create a function called 'front_new_node' that will add a new node to the front of the linked list.

ll.front_new_node(5)
ll.back_new_node(0)
print(ll.head.data) # 5
print(ll.tail.data) # 0
ll.front_new_node(10)
print(ll.head.data) # 10
print(ll.head.next.data) # 5
print(ll.head.next.prev.data) # 10
print(ll.head.next.next.data) # 1


print('\n------------------------------')
print('EXERCISE 4')
print('------------------------------')
# TODO - Create functions called 'remove_tail' and 'remove_head in the LinkedList class that
#  will remove the tail and head from the linked list.

print(ll.head.data) # 10
print(ll.tail.data) # 0
ll.remove_head()
print(ll.head.data) # 5
ll.remove_tail()
print(ll.tail.data) # 4
ll.remove_head()
print(ll.head.data) # 1
ll.remove_tail()
print(ll.tail.data) # 3
ll.remove_head()
print(ll.head.data) # 2
ll.remove_tail()
print(ll.tail.data) # 2
try:
    ll.remove_head()
    print(ll.head.data)
except:
    print('No head is left in the list!')
try:
    ll.remove_tail()
    print(ll.tail.data)
except:
    print('No tail is left in the list!')

# Last two should say:
# No head is left in the list!
# No tail is left in the list!