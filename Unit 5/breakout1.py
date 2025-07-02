# 29

class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution
    
    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    
    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if self.is_caught == True:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")
    
    def add_type(self, new_type):
        self.types.append(new_type)

def get_by_type(my_pokemon, pokemon_type):
    pokemons = []

    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            pokemons.append(pokemon.name)

    return pokemons

def get_evolutionary_line(starter_pokemon):
    evolution = []

    current_pokemon = starter_pokemon

    while current_pokemon:
        evolution.append(current_pokemon.name)
        current_pokemon = current_pokemon.evolution
    
    return evolution

# my_pokemon = Pokemon("Pikachu", ["Electric"])
# squirtle = Pokemon("Squirtle", ["Water"])
# squirtle.print_pokemon()
# squirtle.is_caught = True
# squirtle.print_pokemon()

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()

# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()

# initializing pokemons
# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)

# charizard = Pokemon("Charizard", ["fire", "flying"])
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)

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

# node_1 = Node("Mario")
# node_2 = Node("Luigi")
# node_3 = Node("Wario")
# node_4 = Node("Toad")

# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# node_4.next = None

# print_linked_list(node_1)

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)

# node_one = Node("a")
# node_two = Node("b")

# print(node_one.value) 
# print(node_one.next) 
# print(node_two.value)
# print(node_two.next)
# node_one.next = node_two
#node_two = None

# print(node_one.value)
# print(node_one.next.value)
# print(node_two.value)

#############

class Card():
	def __init__(self, suit, rank, next = None):
		self.suit = suit
		self.rank = rank
		self.next = next
	
	def print_card(self):
		print(f"{self.rank} of {self.suit}")
	
	def is_valid(self):
		suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
		ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

		if self.suit in suits:
			if self.rank in ranks:
				return True
		
		return False
	
	def get_value(self):
		if self.rank == "Ace":
			return 1
		elif self.rank == "Jack":
			return 11
		elif self.rank == "Queen":
			return 12
		elif self.rank == "King":
			return 13
		elif 2 <= int(self.rank) and int(self.rank) <= 10:
			return self.rank
		else:
			return None

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

def sum_hand(hand):
	total = 0
	for card in hand.cards:
		if card.is_valid():
			total += int(card.get_value())
		else:
			return None
	
	return total

def print_hand(starting_card):
	cards = []

	current = starting_card

	while current:
		cards.append(current)
		current = current.next
	
	return cards

# card_one = Card("Hearts", "3")
# card_two = Card("Hearts", "4")
# card_three = Card("Diamonds", "King")

# card_one.next = card_two
# card_two.next = card_three

# print_hand(card_one)

# card_one = Card("Hearts", "3")
# card_two = Card("Hearts", "Jack")
# card_three = Card("Spades", "3")

# hand = Hand()
# hand.add_card(card_one)
# hand.add_card(card_two)
# hand.add_card(card_three)

# sum = sum_hand(hand)
# print(sum)

# card = Card("Clubs", "Ace")
# card.print_card()
# card.suit = "Hearts"
# card.print_card()

# my_card = Card("Hearts", "7")
# print(my_card.is_valid())

# second_draw = Card("Spades", "Joker")
# print(second_draw.is_valid())

# card = Card("Hearts", "7")
# print(card.get_value())

# card_two = Card("Spades", "Jack")
# print(card_two.get_value())