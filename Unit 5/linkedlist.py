class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # we don't know the next so set to None by default

    def insert(self):
        self.next = self
    
a = Node(2)
b = Node(4)
c = Node(6)

a.next = Node(4)
b = None
a.next.next = Node(6)
c = None
# you don't have to create new variables each time

# searching for a node
current = a
while current != None:
    print(current.value)
    current = current.next # always move to the next to afterwards

############
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
    my_str = head.value

    current = head.next

    while current:
        my_str += " -> " + current.value
        current = current.next
    
    print(my_str)

node_1 = Node("Mario")
node_2 = Node("Luigi")
node_3 = Node("Wario")
node_4 = Node("Toad")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = None

print_linked_list(node_1)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

node_one = Node("a")
node_two = Node("b")

print(node_one.value) 
print(node_one.next) 
print(node_two.value)
print(node_two.next)
node_one.next = node_two
node_two = None

print(node_one.value)
print(node_one.next.value)
print(node_two.value)

###########

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
    lst = [head.value]

    current = head.next

    while current:
        lst.append(current.value)
        current = current.next
    
    print(lst)

head = Node(100)
tail = Node(200)

head.next = tail
tail.next = None

print(head.value) 
print(head.next.value) 
print(tail.value) 
print(tail.next) 

middle = Node(150)

head.next = middle
middle.next = tail
tail.next = None
print(head.next.value) 
print(middle.next.value)
print(tail.next) 

node_1 = Node("aries")
node_2 = Node("taurus")
node_3 = Node("gemini")
node_4 = Node("cancer")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = None

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

print_linked_list(node_1)

#############

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def chase_list(head):
    chasing = head.value

    current = head.next

    while current:
        chasing += " chases " + current.value
        current = current.next
    
    return chasing

cat = Node("Tom")
mouse = Node("Jerry")

cat.next = mouse
mouse.next = None

print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next)

dog = Node("Spike")
dog.next = cat

print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
print(mouse.next)

cheese = Node("Gouda")
mouse.next = cheese
print(cat.value)
print(cat.next.value)
print(mouse.next.value)

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))