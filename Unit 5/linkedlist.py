class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # we don't know the next so set to None by default

    def insert(self):
        self.next = self
    
a = Node(2)
#b = Node(4)
#c = Node(6)

a.next = Node(4)
#b = None
a.next.next = Node(6)
#c = None
# you don't have to create new variables each time

# searching for a node
current = a
while current != None:
    print(current.value)
    current = current.next