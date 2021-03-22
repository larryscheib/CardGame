# Import required modules
import itertools
import random

# Define a class to create cards


class Cards:

    # Suits = [1, 2, 3, 4]  = ['Spades', 'Diamonds','Hearts','Clubs']
    SUITS = [1, 2, 3, 4]
    VALUES = range(1, 14)

    def __init__(self):
        pass


# class to categorize cards into a deck

class Deck(Cards):

    def __init__(self):
        Cards.__init__(self)
        self.cardset = []
        self.tempcardset = []

        # make deck
        self.cardset = list(itertools.product(self.SUITS, self.VALUES))

    # method to sort cards
    def sort(self):
        self.tempcardset = sorted(self.cardset, key=lambda value: value[1])
        self.cardset = sorted(self.tempcardset, key=lambda suit: suit[0])
        return self.cardset

    # method to shuffle cards
    def shuffle(self):
        if len(self.cardset) == 52:
            random.shuffle(self.cardset)
        else:
            print("cannot shuffle the cards")
        return self.cardset


''' # Method to remove a card from the deck
        def popcard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS TO DEAL FURTHER"

        cardpopped = self.mycardset.pop()
        return cardpopped
'''

# class for Hand object


class Hand:
    def __init__(self):
        # players hand
        self.playercards = []

        # total value of a hand
        self.handTotal = 0

    # Method to add a card to hand
    def add_card(self, card):
        """
        Args: card:
        """
        self.playercards.append(card)

    # Method to convert suit from int value to alpha value (spades, diamonds, hearts and clubs)
    def conversion(self):

        # suits = ['Spades', 'Diamonds','Hearts','Clubs']  = [1, 2, 3, 4]

        tempstorage = []
        for suit, value in list(self.playercards):
            if value == 11:
                value = 'Jack'
            elif value == 12:
                value = 'Queen'
            elif value == 13:
                value = 'King'
            elif value == 1:
                value = 'ACE'

            if suit == 1:
                tempstorage.append(['Spades', value])
            elif suit == 2:
                tempstorage.append(['Diamonds', value])
            elif suit == 3:
                tempstorage.append(['Hearts', value])
            else:
                tempstorage.append(['Clubs', value])


        self.playercards = tempstorage

    def totalhand(self):
        self.handTotal = 0
        for suit, value in self.playercards:
            self.handTotal += suit * value

    def printtotal(self):
        print("total is ", self.handTotal)

    def gettotal(self):
        return self.handTotal


class Winner:
    def __init__(self, hand1total, hand2total):
        """
        Args: hand1total, hand2total:
        """
        self.hand1total = hand1total
        self.hand2total = hand2total

        self.winner = ''

        if self.hand1total > self.hand2total:
            self.winner = 'player1 wins'
        elif self.hand1total == self.hand2total:
            self.winner = 'we have a tie'
        else:
            self.winner = 'player2 wins'

    def getwinner(self):
        return self.winner

# Driver Code for Creating objects

# create cards


objCards = Cards()


# generate a deck based on cards
objDeck = Deck()
deckOfCards = objDeck.cardset

# sort deck


sortedDeck = objDeck.sort()


# shuffle deck


shuffledCards = objDeck.shuffle()


# create player 1 hand


player1Hand = Hand()


# create player 2 hand


player2Hand = Hand()



# deal 3 card hands to both players


for x in range(0, 3):
    playerCard1 = shuffledCards.pop(0)
    player1Hand.add_card(playerCard1)
    playerCard2 = shuffledCards.pop(0)
    player2Hand.add_card(playerCard2)


# generate total for hand one


player1Hand.totalhand()


# generate total for hand two


player2Hand.totalhand()


# determine winner

winner = Winner(player1Hand.gettotal(), player2Hand.gettotal())

print('\n', winner.getwinner(), '\n')


# convert suits from numeric to alpha and values


player1Hand.conversion()
print('player1Hand \n',player1Hand.playercards,'\n')


player2Hand.conversion()
print('player2Hand \n',player2Hand.playercards,'\n')