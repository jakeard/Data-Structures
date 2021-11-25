'''
Implement a stack to keep track of who is using 
what plates, and in what order the plates are in. 
The list of plates and people is given.
'''

plates = ['Flowers', 'Dora', 'Plastic', 'Glass', 'Plain']
bob = None
sue = None
dylan = None


print('\n------------------------------')
print('EXERCISE 1')
print('------------------------------')
# Bob and Sue use a plate

# TODO: Put code here

print(bob) # Animal plate
print(sue) # Glass Plate
print(plates) # ['Flower plate', 'Dora plate', 'Plastic plate']


print('\n------------------------------')
print('EXERCISE 2')
print('------------------------------')
# Dylan uses a plate, Bob uses a plate, and Sue uses a plate, and then Bob puts his back, then Sue puts hers back

# TODO: Put code here

print(dylan) # Plastic plate
print(bob) # Dora plate
print(sue) # Flower plate
print(plates) # ['Dora plate', 'Flower plate']