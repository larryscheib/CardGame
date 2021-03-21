# Import required modules
import itertools, random

# Define a class to create cards
class Cards:

   # suits = [1, 2, 3, 4]  = ['Spades', 'Diamonds','Hearts','Clubs']

   global suits, values

   suits = [4,3,2,1]
   values = range(1,14)

   def __init__(self):
      pass

# class to create deck of cards

class Deck(Cards):
   def __init__(self):
      Cards.__init__(self)
      self.mycardset = []
      self.cardset = []

      # make deck
      self.mycardset  = list(itertools.product(suits,values))

   # method to sort cards
   def sort(self):
      self.cardset = sorted(self.mycardset, key=lambda x: x[1])
      return sorted(self.cardset, key=lambda x: x[0])

   # method to shuffle cards
   def shuffle(self):
      if len(self.mycardset) < 52:
         print("cannot shuffle the cards")
      else:
         random.shuffle(self.mycardset)
         return self.mycardset

   # Method to remove a card from the deck
   def popCard(self):
      if len(self.mycardset) == 0:
         return "NO CARDS TO DEAL FURTHER"
      else:
         cardpopped = self.mycardset.pop()
         return (cardpopped)


class Hand:
   def __init__(self):
      self.playercards = []

      # total value of a hand
      self.total = 0

   # Method to add a card to hand
   def add_card(self,card):
      self.playercards.append(card)

   # Method to convert suit from int value to alpha value (spades, diamonds, hearts and clubs)
   def conversion(self):

      # suits = ['Spades', 'Diamonds','Hearts','Clubs']  = [1, 2, 3, 4]

      tempStorage = []
      for a, b in list(self.playercards):
         if a == 1:
            tempStorage.append(['Spades',b])
         elif a==2:
            tempStorage.append(['Diamonds',b])
         elif a==3:
            tempStorage.append(['Hearts',b])
         else:
            tempStorage.append(['Clubs',b])

      self.playercards = tempStorage


   def totalhand(self):
      for suit, value in self.playercards:
         self.total += suit * value

   def printTotal(self):
      print ("total is ",self.total)

   def getTotal(self):
      return self.total


class Winner:
   def __init__(self, hand1total, hand2total):
      self.hand1total = hand1total
      self.hand2total = hand2total

      if (self.hand1total > self.hand2total):
         print("player1 wins")
      elif(self.hand1total == self.hand2total):
         print("we have a tie")
      else:
         print("player2 wins")

# Driver Code
# Creating objects

# create cards
objCards = Cards()

# generate a deck based on cards
objDeck = Deck()

# deck object
deckOfCards = objDeck.mycardset
print("deck of cards: ","\n", deckOfCards)


# sort deck
sortedDeck = objDeck.sort()
print("sorted: ","\n", sortedDeck)


# Creating shuffle object
#objShuffleCards = ShuffleCards()

# shuffle deck
shuffledCards = objDeck.shuffle()
print("shuffled: ","\n", shuffledCards)


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


# generate total hand one
player1Hand.totalhand()
print("\nhand 1: ",player1Hand.playercards)
print("hand 1 total:", player1Hand.getTotal())

# generate total hand two
player2Hand.totalhand()
print("\nhand 2 ",player2Hand.playercards)
print("hand 2 total:", player2Hand.getTotal(), '\n')

# determine winner
Winner(player1Hand.getTotal(), player2Hand.getTotal())
print ('\n')


# convert suits from numeric to alpha values
player1Hand.conversion()
print('player1Hand \n',player1Hand.playercards,'\n')


player2Hand.conversion()
print('player2Hand \n',player2Hand.playercards,'\n')

