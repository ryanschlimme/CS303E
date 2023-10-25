# Hand.py
# Ryan Schlimme
# rjs4499
# CS 303E
# 52415
#
# 24 October 2023
# This program creates a Hand class to evaluate poker hands generated using the Card and Deck class 
# which are supplied. It is possible to generate hands by dealing 5 cards from a deck or by specifying 
# the five cards as a list of card specifiers via the Card class. Users can import Hand, create a new 
# deck, shuffle it, deal a hand or create a hand from a list of card specifiers, and evaluate the hand.

# Relavent Hands:
# pair: two cards of the same rank, e.g., two Kings;
# two pairs: two pairs, but not all the same rank, e.g., two 3s and two Kings;
# three of a kind: three cards of the same rank, e.g., three 10s;
# four of a kind: four cards of the same rank, e.g., four Aces
# full house: one pair and three of a kind;
# flush: five cards all in one suit, e.g, five Spades;
# straight: five cards in consecutive rank order, e.g., 7, 8, 9, 10, Jack (of any suit). 
#           Notice that Ace can be high or low.;
# straight flush: a straight, all of the same suit;
# Royal flush: 10, Jack, Queen, King, Ace all of the same suit;
# nothing: none of the above.

""" This file includes a class Hand which implements a hand of five playing
    cards, where cards are defined in the Card class.   

    The Hand class defines the following methods:

    Hand( source, fromDeck ):  creates a new hand object of 5 Cards. This happens
         in one of two ways depending on the value of fromDeck: 
         (1) if fromDeck is True, deal 5 cards from an existing deck
             passed as source, 
         (2) if fromDeck is not True, create the cards from a list of 5 card 
             specifiers passed as source, e.g., ("2S", "9S", "TC", "AH", "4D") 
             will create a hand containing the 2 of Spades, 9 of Spades, 10 of Clubs, 
             Ace of Hearts, and 4 of Diamonds.  Generating a single card from a 
             spec is implemented in the Card class.  You need to check that this
             list is legal (contains exactly 5 legal card specifiers, all distinct).
    h.__str__(): generate the print representation of Hand h, using the
         str function on each of the individual Cards it contains (see the Deck
         class for a model for this);
    h.getCard( i ): recall that h is a hand of 5 Cards.  This provides a 
         way of getting the ith card from the hand, for example, to iterate 
         through the hand in a loop. 

    This file also contains a number of other functions (outside the class), mainly
    to allow evaluating a hand in the sense of playing Poker.  You can have as many
    functions as you need, but you must have the function evaluateHand( hand ). 
    Given a hand, it prints the hand and then the "evaluation" of the hand in 
    the sense of a Poker hand.  This is described in detail in the assignment description.   

"""

################################################################################
#                                                                              #
#                                 Hand Class                                   #
#                                                                              #
################################################################################

# I don't need to import Card, since Deck already does.
from Deck import *
from Card import *

def isLegalCardList( l ):
    """ Check that list l contains 5 legal card specifiers, 
        all distinct. You can assume that it's a list. """
    if len(l) != 5: return False        # if list does not contain exactly 5 specifiers, FALSE
    for i in range(0, len(l)):          # iterate through list
        z = l[i]                        # define primary comparator
        for j in range(i+1, len(l)):    # iterate through all other cards
            x = l[j]                    # define secondary compartor
            if z == x:                  # if secondary comparator equals the primary comparator, FALSE 
                return False
    x = []                              # define empty results list
    for i in l:
        x.append(isLegalCardSpecifier(i))   # check if specifier is valid
    if False in x:                      # if any card specifier is invalid, FALSE
        return False
    else:
        return True                     # if list contains 5 legal, non-duplicate specifiers, TRUE
    

class Hand:
    def __init__(self, source, fromDeck = True):
        """ A hand is simply a list of 5 cards, dealt from the deck
            or given as a list of five card specifiers.  If fromDeck
            is True, expect to deal from a deck passed as source. 
            If False, expect source to be a list of five Card specifiers.
            Create the hand from the specified cards.
        """
        if fromDeck == True:
            if ( len(source) < 5 ):
                print ( "Not enough cards left!" )
                return None
            self.__cards = []
            for i in range(5):
                card = source.deal()              # deal next card
                self.__cards.append(card)         # append it to the hand
        elif not isLegalCardList( source ):
            print("Illegal card list provided.")
        else:
            self.__cards = [Card(c) for c in source]

    def __str__(self):
        result = ""
        for c in self.__cards:
            result += str(c) + "\n"
        return result
        
    def getCard( self, i ):
        """ Get the ith card from the hand, where 
            i in [0..4]. Return None if i is not
            legal. """
        if i > 4 or i < 0: return None
        else:
            return self.__cards[i]
            
################################################################################
#                                                                              #
#                                Evaluate Hand                                 #
#                                                                              #
################################################################################

def processHand( hand ):
    """ Given a poker hand, create and return two lists which
        record the ranks and suits in the hand. """
    myRanks = [0] * 13    # a list of 13 zeros
    mySuits = [0] * 4     # a list of 4 zeros
    myCards = [str(hand.getCard(i)) for i in range(5)]
    for z in range(5):
        for rankIndex in range(13):
            if RANKNAMES[rankIndex] in myCards[z]:
                myRanks[rankIndex] += 1
        for suitIndex in range(4):
            if SUITNAMES[suitIndex] in myCards[z]:
                mySuits[suitIndex] += 1
    return myRanks, mySuits

# You'll need to define all of the auxiliary functions called by
# evaluateHand.  Notice that these auxiliary functions don't all
# need both myRanks and mySuits, but I decided to pass them both
# just to make the interface more uniform.  You can change that 
# if you want to.

def hasPair( myRanks, mySuits ):
    if 2 in myRanks:
        return True
    else:
        return False
    
def hasTwoPair(myRanks, mySuits):
    if 2 not in myRanks:
        return False
    count = 0
    for i in range(4):
        if myRanks[i] == 2:
            count += 1
    if count == 2:
        return True
    else:
        return False
    
def hasThreeOfAKind(myRanks, mySuits):
    if 3 in myRanks:
        return True
    else:
        return False
    
def hasFourOfAKind(myRanks, mySuits):
    if 4 in myRanks:
        return True
    else:
        return False
    
def hasFullHouse(myRanks, mySuits):
    if 2 and 3 in myRanks:
        return True
    else:
        return False
    
def hasFlush(myRanks, mySuits):
    if 5 in mySuits:
        return True
    else:
        return False
    
def hasStraight(myRanks, mySuits):
    if 2 in myRanks:
        return False
    if 3 in myRanks:
        return False
    if 4 in myRanks:
        return False
    if 5 in myRanks:
        return False
    indices = []
    for i in range(13):
        if myRanks[i] == 1:
            indices.append(i)
    indices = [i - min(indices) for i in indices]
    if indices == [0,1,2,3,4] or indices == [0,1,2,3,12]:
        return True
    else:
        return False

def hasStraightFlush(myRanks, mySuits):
    if hasStraight(myRanks, mySuits) == True and hasFlush(myRanks, mySuits) == True: return True
    else: return False

def hasRoyalFlush(myRanks, mySuits):
    if hasFlush(myRanks, mySuits) == True and hasStraight(myRanks, mySuits) == True:
        if myRanks[8] == 1 and myRanks[9] == 1 and myRanks[10] == 1 and myRanks[11] == 1 and myRanks[12] == 1:
            return True
    else:
        return False

# Add other recognizers here; evaluateHand tells you which ones you
# need.  I suggest doing them in "reverse order" so you define the 
# lowest hands first. Hopefully, you'll see why as you code them!

def evaluateHand( hand ):
    myRanks, mySuits = processHand( hand )
    print( hand )
    if hasRoyalFlush( myRanks, mySuits ):
        print( "Royal Flush" )
    elif hasStraightFlush( myRanks, mySuits ):
        print( "Straight Flush" )
    elif hasFourOfAKind( myRanks, mySuits ):
        print( "Four of a kind" )
    elif hasFullHouse( myRanks, mySuits ):
        print( "Full House" )
    elif hasFlush( myRanks, mySuits ):
        print( "Flush" )
    elif hasStraight( myRanks, mySuits ):
        print( "Straight" )
    elif hasThreeOfAKind( myRanks, mySuits ):
        print( "Three of a kind" )
    elif hasTwoPair( myRanks, mySuits ):
        print( "Two pair" )
    elif hasPair( myRanks, mySuits ):
        print( "Pair" )
    else:
        print( "Nothing" )

# This is some test code.  You can modify this or write your
# own.  You certainly should test additional hands. You can run 
# this in interactive mode with:
# 
# from Hand import *
# TestCode()
#
# You can also run this in batch mode by uncommenting the call to:
# TestCode()
#
# and running:
# 
# python3 Hand.py              # or whatever the python command is
#                              # is on your system. 

def TestCode():
    print("\nGenerating and printing deck")
    d = Deck()
    print(d)
    print("\nShuffling deck and printing deck")
    d.shuffle()
    print(d)

    print("\nGenerating hand from deck")
    h = Hand(d, True)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["as", "ad", "ah", "ac", "2d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["AS", "2S", "3C", "4H", "5D"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["2s", "9S", "tc", "AH", "4d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

#TestCode()