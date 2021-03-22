import functools, time

from main import Deck, Hand, Winner
from ptest.decorator import TestClass

@TestClass(run_mode="parallel")  # the test cases in this class will be executed by multiple threads

class test_CardGame_pytest:
    def test_Deck(self, list2=None, list1=None):
        objDeck = Deck()

        # test that new deck is 52 cards

        deckOfCards = objDeck.cardset
        assert len(deckOfCards) == 52


        # test that values are in correct sorted location


        sortedDeck = objDeck.sort()


        print("sortedCards ", sortedDeck)
        assert sortedDeck[0:1][0:1] == [(1, 1)]
        assert sortedDeck[0:10][9:10] == [(1, 10)]
        assert sortedDeck[0:13][12:13] == [(1, 13)]
        assert sortedDeck[0:26][25:26] == [(2, 13)]
        assert sortedDeck[0:39][38:39] == [(3, 13)]
        assert sortedDeck[0:52][51:52] == [(4, 13)]

        # shuffle deck


        shuffledCards = objDeck.shuffle()
        print("shuffledCards ",shuffledCards)


        list1 = list(shuffledCards)


        # test second shuffle

        secondShuffle = objDeck.shuffle()
        print('secondShuffle ',secondShuffle)


        list2 = list(secondShuffle)

        # shuffles should be unique (is it even possible to have back to back shuffles the same, I don't think so)

        isSame = functools.reduce(lambda x, y :x and y, map(lambda p, q : p==q, list1,list2),True)

        assert isSame == False

        # create hand
        playerHand = Hand()

        # initial hand should always score to zero
        assert playerHand.gettotal() == 0

        # add card from shuffled deck
        playerCard = shuffledCards.pop(0)
        playerHand.add_card(playerCard)


        # total hand
        playerHand.totalhand()

        # added first card implies hand value will be greater than 0
        assert playerHand.gettotal() > 0


        # size of shuffledCards should now be 51
        assert len(shuffledCards) == 51

        # test method add_card to verify hand is in fact 35

        newPlayer1Hand = Hand()
        newPlayer1Hand.add_card((4,2))
        newPlayer1Hand.add_card((1,11))
        newPlayer1Hand.add_card((4,4))
        newPlayer1Hand.totalhand()

        assert newPlayer1Hand.gettotal() == 35


        # manually create another hand that totals 37


        newPlayer2Hand = Hand()
        newPlayer2Hand.add_card((4,2))
        newPlayer2Hand.add_card((3,7))
        newPlayer2Hand.add_card((1,8))
        newPlayer2Hand.totalhand()
        assert newPlayer2Hand.gettotal() == 37


        # test for Winner class; winner should be hand two


        winner = Winner(newPlayer1Hand.gettotal(), newPlayer2Hand.gettotal())
        assert winner.getwinner() == 'player2 wins'


        # test conversion method where suits = [1, 2, 3, 4]  = ['Spades', 'Diamonds','Hearts','Clubs']

        newPlayer1Hand.conversion()

        assert newPlayer1Hand.playercards[1][1] == 'Jack'

        assert newPlayer1Hand.playercards[0][0] == 'Clubs'
        assert newPlayer1Hand.playercards[1][0] == 'Spades'
        assert newPlayer1Hand.playercards[2][0] == 'Clubs'

test_CardGame_pytest().test_Deck()
