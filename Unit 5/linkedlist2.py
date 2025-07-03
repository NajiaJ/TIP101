class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

def add_first(head, new_node):
    new_node.next = head
    return new_node

def get_tail(head):
	current = head
    
	while current:
		current = current.next
		if current.next == None:
			return current.value

def ll_replace(head, original, replacement):
	current = head

	while current:
		if current.value == original:
			current.value = replacement
		current = current.next

def listify_first_n(head, n):
	lst = []
	current = head
	count = 0

	while current and count < n:
		lst.append(current.value)
		current = current.next
		count += 1
	
	return lst

def ll_insert(head, val, i):
	current = head
	count = 0

	if i == 0:
		head.next = val

	while current and count <= i:
		current.next = val
		count += 1
	
	return current

def print_reverse(tail):
	current = tail
	my_str = ""

	while current != None:
		my_str += current.value + " "
		current = current.prev
	
	print(my_str)

# node_1 = Node("Jigglypuff")
# node_2 = Node("Wigglytuff")

# node_1.next = node_2
# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)

# Using the Linked List from Problem 2
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)

# print(node_1.value, "->", node_1.next.value)

# node_1 = Node("Jigglypuff")
# node_2 = Node("Wigglytuff")
# node_3 = Node("Ditto")
# node_1.next = node_2
# node_2.next = node_3
# head = node_1
# tail = get_tail(node_1)
# print(tail)

# num3 = Node(5)
# num2 = Node(6, num3)
# num1 = Node(5, num2)
# # initial linked list: 5 -> 6 -> 5

# head = num1
# ll_replace(head, 5, "banana")
# # updated linked list: "banana" -> 6 -> "banana"

# linked list: a -> b -> c
# c = Node("c")
# b = Node("b", c)
# a = Node("a", b)

# head = a
# lst = listify_first_n(head,2)
# print(lst)

# # linked list: j -> k -> l 
# l = Node("l")
# k = Node("k", l)
# j = Node("j", k)
# head2 = j
# lst2 = listify_first_n(head2,5)
# print(lst2)

poliwrath = Node("Poliwrath")
poliwhirl = Node("Poliwhirl")
poliwag = Node("Poliwag")

poliwag.next = poliwhirl
poliwhirl.prev = poliwag
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl

print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)
print_reverse(poliwrath)