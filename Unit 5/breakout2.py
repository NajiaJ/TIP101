class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
    current = head
    if current == None:
        return None

    while current:
        current = current.next
        if current.next == None:
            return current.value

# def listify_first_n(head, n):
# 	lst = []
    
#     current = head
#     count = 0
    
#     while current.next and count <= n:
#         lst.append(current.value)
#         count += 1
        
#     return lst

# node_1 = Node("Jigglypuff")
# node_2 = Node("Wigglytuff")

# node_1.next = node_2
# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)

# linked list: num1->num2->num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")

num1.next = num2
num2.next = num3

head = num1
tail = get_tail(num1)
print(tail)