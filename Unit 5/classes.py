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

############################################################################
class Player:
    def __init__(self, character, kart, opponent = None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
    
    def get_player(self):
        return f"{self.character} driving the {self.kart}"
    
    def set_player(self, name):
        valid_names = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]

        if name in valid_names:
            self.character = name
            print("Character updated")
        else:
            print("Invalid character")
    
    def add_item(self, item_name):
        playable_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]

        if item_name in playable_items:
            self.items.append(item_name)
    
    def print_inventory(self):
        inventory = {}

        for item in self.items:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
        
        if len(inventory) == 0:
            print("Inventory empty")
        else:
            inventory_str = [f"{item}: {count}" for item, count in inventory.items()]
            print("Inventory:", ", ".join(inventory_str))

def print_results(race_results):
    counter = 1
    for position in race_results:
        print(str(counter) + ". " + position.character)
        counter += 1

def get_place(my_player):
    positions = 1

    current_player = my_player.ahead

    while current_player:
        positions += 1
        current_player = current_player.ahead
    
    return positions

player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Piranhna Prowler")

print("Match: " + player_one.get_player() + " vs " + player_two.get_player())

print(player_one.get_player())

player_one.kart = "Dolphin Dasher"

print(player_one.get_player())

player_one.set_player("Peach")
player_two.set_player("Kermit")

player_one = Player("Yoshi", "Dolphin Dasher") # items = []
player_one.add_item("red shell") # items = ["red shell"]
player_one.add_item("super star") # items = ["red shell", "super star"]
player_one.add_item("super smash") # items = ["red shell", "super star"]
print(player_one.items)

player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
print(player1_rank)

player2_rank = get_place(peach)
print(player2_rank)

player3_rank = get_place(mario)
print(player3_rank)