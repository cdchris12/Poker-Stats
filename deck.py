import random
from copy import deepcopy
from operator import itemgetter

secure_random = random.SystemRandom()

class deck:
    class card:
        def __init__(self, suit, value, name, verbose=False):
            self.suit = suit
            self.value = value
            self.name = name
            self.verbose = verbose
        # End def

        def __repr__(self):
            return '%s of %s' % (self.name, self.suit)
        # End def
    # End class

    class hand:
        def __init__(self, cards, verbose=False):
            self.cards = cards
            self.suits = {}
            self.values = []
            self.size = len(cards)
            self.verbose = verbose

            for card in cards:
                if card.suit not in self.suits:
                    self.suits[card.suit] = 1
                else:
                    self.suits[card.suit] += 1
                # End if/else block

                self.values.append(card.value)
            # End for
        # End def

        def __repr__(self):
            string = ''
            for card in self.deck:
                string += str(card) + ', '
            # End for

            return string
        # End def

        def add(self, cards):
            if type(cards) == type([]):
                for card in cards:
                    if card.suit not in self.suits:
                        self.suits[card.suit] = 1
                    else:
                        self.suits[card.suit] += 1
                    # End if/else block

                    self.values.append(card.value)
                    self.cards.append(card)
                    if self.verbose: print "Added %s!" % card
                # End for
            else:
                if cards.suit not in self.suits:
                    self.suits[cards.suit] = 1
                else:
                    self.suits[cards.suit] += 1
                # End if/else block

                self.values.append(cards.value)
                self.cards.append(cards)
                if self.verbose: print "Added %s!" % cards
            # End if/else block
        # End def

        def remove(self, cards):
            if type(cards) == type([]):
                for card in cards:
                    self.suits[card.suit] -= 1
                    self.values.remove(card.value)
                    self.cards.remove(card)
                    if self.verbose: print "Removed %s!" % card
                # End for
            else:

                self.suits[cards.suit] -= 1
                self.values.remove(cards.value)
                self.cards.remove(cards)
                if self.verbose: print "Removed %s!" % cards
            # End if/else block
        # End def

        def is_flush(self):
            for suit in self.suits:
                if self.suits[suit] >= 5:
                    return True
            else:
                return False
            # End for/else block
        # End def

        def is_straight(self):

            def count_straight(values):
                counter = 1
                for i, value in enumerate(values):
                    if i == 0:
                        continue
                    elif values[i-1] == value - 1:
                        counter += 1
                    else:
                        counter = 1
                    # End if/else block

                    if counter == 5: return True
                else:
                    return False
                # End for/else block
            # End def

            if 1 in self.values and 13 in self.values:
                values_low = sorted(self.values)
                values_high = deepcopy(self.values)
                values_high.remove(1)
                values_high.append(14)
                values_high = sorted(values_high)

                if count_straight(values_low): return True
                elif count_straight(values_high): return True
                else: return False
            else:
                if count_straight(sorted(self.values)): return True
                else: return False
            # End if/else block
        # End def

        def score(self):
            # Check matches in decreasing order, and return the best (first) one.

            flush = False
            straight = False
            pair = self.has_pair()

            if self.size >= 5:
                flush = self.is_flush()
                # Check flush first; if it is a flush, it can't have pairs.

                straight = self.is_straight()
                # Self explainatory

                if flush:
                    if straight:
                        if 1 in self.values \
                        and 13 in self.values \
                        and 12 in self.values \
                        and 11 in self.values \
                        and 10 in self.values:
                            # Found Royal Flush
                            if self.verbose: print 'Found a Royal Flush!'
                            return 'Royal Flush'
                        else:
                            # Found Straight Flush
                            if self.verbose: print 'Found a Straight Flush!'
                            return 'Straight Flush'
                        # End if/else block
                    else:
                        # Possible Flush
                        pass
                    # End if/else block
                # End if
            # End if

            if pair == 'Four of a Kind':
                # Found Four of a kind
                if self.verbose: print 'Found a Four of a Kind!'
                return 'Four of a Kind'
            elif pair == 'Full House':
                # Found Full House
                if self.verbose: print 'Found a Full House!'
                return 'Full House'
            elif flush:
                # Found a Flush
                if self.verbose: print "Found a Flush!"
                return "Flush"
            elif straight:
                # Found a Straight
                if self.verbose: print 'Found a Straight!'
                return 'Straight'
            elif pair == 'Three of a Kind':
                # Found Three of a Kind
                if self.verbose: print 'Found Three of a Kind!'
                return 'Three of a Kind'
            elif pair == 'Two Pair':
                # Found Two Pair
                if self.verbose: print 'Found Two Pair!'
                return 'Two Pair'
            elif pair == 'Pair':
                # Found a Pair
                if self.verbose: print 'Found a Pair!'
                return 'Pair'
            else:
                # Found a High Card
                if self.verbose: print 'Found a High Card!'
                return 'High Card'
            # End if/else block
        # End def

        def has_pair(self):
            if self.size == 1: return False

            count = {}
            for value in self.values:
                if value in count:
                    count[value] += 1
                else:
                    count[value] = 1
                # End if/else block
            # End for

            sorted_count = sorted(count.items(), key=itemgetter(1), reverse=True)
            # List of tuples: ('value', number_of_occurances)

            for i, item in enumerate(sorted_count):
                if item[1] == 4:
                    return 'Four of a Kind'
                elif item[1] == 3:
                    try:
                        if sorted_count[i+1][1] >= 2:
                            return 'Full House'
                    except IndexError, e:
                        # If we reach the last index, we know we have Three of a Kind
                        return 'Three of a Kind'
                    else:
                        return 'Three of a Kind'
                elif item[1] == 2:
                    try:
                        if sorted_count[i+1][1] == 2:
                            return 'Two Pair'
                    except IndexError, e:
                        # If we reach the last index, we know we have a Pair
                        return 'Pair'
                    else:
                        return 'Pair'
                # End if/else block
            else:
                return False
            # End for/else block
        # End def
    # End class

    def __init__(self, verbose=False):
        if verbose: print 'Generating a deck of cards to use...'
        self.suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        self.values = range(1, 14)
        self.names = [ 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.verbose = verbose

        self.deck = []
        for suit in self.suits:
            for i, value in enumerate(self.values):
                self.deck.append( deck.card(suit, value, self.names[i]) )
            # End for
        # End for
        if self.verbose:
            print 'Finished card deck generation!'
            print 'Generated deck\'s contents are:\n'
            print self.deck
        # End if
    # End def

    def __repr__(self):
        string = ''
        for card in self.deck:
            string += str(card) + ', '
        # End for

        return string
    # End def

    def get_hand(self, num_cards, verbose=False):
        hand_list = []

        for i in range(num_cards):
            rand = secure_random.choice(self.deck)
            while rand in hand_list:
                rand = secure_random.choice(self.deck)
            # End while

            hand_list.append(rand)
        # End for

        return deck.hand(hand_list, verbose)
    # End def
# End class
