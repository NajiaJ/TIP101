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
    result = []

    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            result.append(pokemon.name)
    
    return result

def get_evolutionary_line(starter_pokemon):
    evolution_line = []
    
    first_pokemon = starter_pokemon

    while first_pokemon:
        evolution_line.append(first_pokemon.name)
        first_pokemon = first_pokemon.evolution

    return evolution_line

# TESTING
my_pokemon = Pokemon("Pikachu", ["Electric"])
squirtle = Pokemon("Squirtle", ["Water"])
squirtle.is_caught = True
squirtle.print_pokemon()

my_pokemon = Pokemon("Rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()

my_pokemon = Pokemon("Rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()

jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)

############################################################################
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

        if self.suit in suits and self.rank in ranks:
            return True
        else:
            return False
    
    def get_value(self):
        if self.rank.isdigit():
            return int(self.rank)
        
        rank_values = {"Ace": 1, "Jack": 11, "Queen": 12, "King": 13}

        return rank_values.get(self.rank, None)

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
            total += card.get_value()
        else:
            return None
    
    return total

def print_hand(starting_card):
    order = []

    current_card = starting_card

    while current_card:
        order.append(current_card)
        current_card = current_card.next
    
    return order


card = Card("Hearts", "Ace")
card.print_card()

my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print_hand(card_one)