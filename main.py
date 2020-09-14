#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
dealer = [[],[]] #hand, value
player = [[],[]] #hand, value
table = [[],[]]
playing = True


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self,RANKS,SUITE):
        self.RANKS = RANKS
        self.SUITE = SUITE
        self.deck = []



    def build_deck(self):
        for suit in SUITE:
            for rank in RANKS:
                phrase = rank + ' of ' + suit
                self.deck.append(phrase)
        return self.deck

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        count = 0
        while count != 52:
            player[0].append(self.deck[0])
            self.deck.pop(0)
            dealer[0].append(self.deck[0])
            self.deck.pop(0)
            count += 2

        return table






class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,dealer,table):
        self.dealer = dealer
        self.table = table #first list player hand,second list dealer

    def add(self):
        table[1].append(dealer[0][0])
        dealer[0].pop(0)
        return table

    def remove(self):
        for card in range(len(table[0])):
            dealer[0].append(card)
            table[0].pop(0)
        for card in range(len(table[1])):
            dealer[0].append(card)
            table[1].pop(0)
        player[1] = []
        dealer[1] = []







class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,player,table):
        self.player = player
        self.table = table

    def name(self):
        name = input('What is your Name? ')
        return f"Hello {name}, let's play!"

    def add(self):
        table[0].append(player[0][0])
        player[0].pop(0)
        return table

    def remove(self):
        for card in range(len(table[0])):
            player[0].append(card)
            table[0].pop(0)
        for card in range(len(table[1])):
            player[0].append(card)
            table[1].pop(0)
        player[1] = []
        dealer[1] = []


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
d = Deck(RANKS,SUITE)
h = Hand(dealer,table)
p = Player(player,table)
d.build_deck()
d.shuffle()
d.deal()
p.name()

while playing:
    hit = input('Hit or Quit?')
    if hit.lower() == 'hit' or hit.lower() == 'h':
        h.add()
        p.add()
        print(table)
        try:
            if table[0][0][0] in values.keys() or table[1][0][0] in values.keys():
                try:
                    player[1].append(values[table[0][0][0]])
                except KeyError:
                    player[1] = [10]
                try:
                    dealer[1].append(values[table[1][0][0]])
                except KeyError:
                    dealer[1] = [10]
                if player[1] > dealer[1]:
                    print('You won this hand!')
                    p.remove()
                elif player[1] < dealer[1]:
                    print('Sorry, you lose this hand!')
                    h.remove()
                else:
                    print('TIE! WAR HAS BEEN DECLARED')
                    print(player[1])
                    print(dealer[1])
                    i = 4
                    while player[1] == dealer[1]:
                        player.append([player[0][0]]) #adds another nested for hidden
                        table[0].append('FACEDOWN')
                        player.append([player[0][0]]) #adds another nested for hidden
                        table[0].append('FACEDOWN')
                        player.append([player[0][0]]) #adds another nested for hidden
                        table[0].append('FACEDOWN')
                        p.add()
                        dealer.append([dealer[0][0]]) #adds another nested list for hidden
                        table[1].append('FACEDOWN')
                        dealer.append([dealer[0][0]]) #adds another nested list for hidden
                        table[1].append('FACEDOWN')
                        dealer.append([dealer[0][0]]) #adds another nested list for hidden
                        table[1].append('FACEDOWN')
                        h.add()
                        print(table)
                        try:
                            player[1] = values[table[0][i][0]]
                        except KeyError:
                            player[1] = [10]
                        try:
                            dealer[1] = values[table[1][i][0]]
                        except KeyError:
                            dealer[1] = [10]
                        i += 4
                        if player[1] > dealer[1]:
                            print("You won the hand!")
                            p.remove()
                            break
                        elif player[1] < dealer[1]:
                            print("Sorry, you lose the hand!")
                            h.remove()
                            break
        except TypeError:
            print("TypeError occured: can't compare list and int ")
            print(f'table: {table}')
            print(f'player varaible: {player[1]}')
            print(f'dealer varaible: {dealer[1]}')


    elif hit.lower() == 'quit' or hit.lower() == 'q':
        print(f"player[0]: {player[0]}")
        print(f"player[1]: {player[1]}")
        print(f"table: {table}")
        print(f"dealer[0]: {dealer[0]}")
        print(f"dealer[1]: {dealer[1]}")
        playing = False
        break

    elif len(player[0]) == 52 or len(dealer[0]) == 52:
        if len(player[0]) > len(dealer[0]):
            print('Congradulations! You won the game!')
        else:
            print('Sorry, you lose!')
        playing = False
    else:
        print('Try Again. HIT or QUIT')









#
# Use the 3 classes along with some logic to play a game of war!
