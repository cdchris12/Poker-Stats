#!/usr/bin/python

import argparse
import random
import sys
import time
import os
from operator import itemgetter
from multiprocessing import Pool, TimeoutError, cpu_count, Process, Queue

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num_hands', type=int, help='The number of hands to simulate drawing.')
parser.add_argument('-c', '--num_cards', type=int, choices=range(5, 14), help='The number of cards to draw each hand. Must be between 5 and 13.')
parser.add_argument('-m', '--multiprocessing', type=int, default=0, choices=range(2, cpu_count()+1), help='Enter the degree of multiprocessing you\'d like to use for significantly faster computation of large statistical analyses.')
parser.add_argument('-v', '--verbose', action='store_true', help='Show more information as the results are being computed.')
args = parser.parse_args()

secure_random = random.SystemRandom()

class deck:
    class card:
        def __init__(self, suit, value, name):
            self.suit = suit
            self.value = value
            self.name = name
        # End def

        def __repr__(self):
            return '%s of %s' % (self.name, self.suit)
        # End def
    # End class

    class hand:
        def __init__(self, cards):
            self.cards = cards
            self.suits = []
            self.values = []
            self.size = len(cards)

            for card in cards:
                if card.suit not in self.suits: self.suits.append(card.suit)
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

        def is_flush(self):
            if len(self.suits) == 1:
                return True
            else:
                return False
            # End for/else block
        # End def

        def is_straight(self):
            if 1 in self.values:
                values_low = sorted(self.values)
                values_high = self.values
                values_high.remove(1)
                values_high.append(14)
                values_high = sorted(values_high)

                counter = 1
                for i, value in enumerate(values_low):
                    if i == 1:
                        continue
                    elif values_low[i-1] == value - 1:
                        counter += 1
                    else:
                        counter = 1
                    # End if/else block

                    if counter == 5: return True
                else:
                    counter = 1
                # End for/else block

                for i, value in enumerate(values_high):
                    if i == 1:
                        continue
                    elif values_high[i-1] == value - 1:
                        counter += 1
                    else:
                        counter = 1
                    # End if/else block

                    if counter == 5: return True
                else:
                    return False
                # End for/else block
            else:
                sorted_values = sorted(self.values)

                counter = 1
                for i, value in enumerate(sorted_values):
                    if i == 1:
                        continue
                    elif sorted_values[i-1] == value - 1:
                        counter += 1
                    else:
                        counter = 1
                    # End if/else block

                    if counter == 5: return True
                else:
                    return False
                # End for/else block
            # End if/else block
        # End def

        def score(self):
            # Check matches in decreasing order, and return the best (first) one.

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
                        if args.verbose: print 'Found a Royal Flush!'
                        return 'Royal Flush'
                    else:
                        # Found Straight Flush
                        if args.verbose: print 'Found a Straight Flush!'
                        return 'Straight Flush'
                    # End if/else block
                else:
                    # Found Flush
                    if args.verbose: print 'Found a Flush!'
                    return 'Flush'
                # End if/else block
            else:
                unique = list(set(self.values))
                num_unique = len(unique)
                num_same = self.size - num_unique
                # Tells us how many unique cards we have in this hand.

                for val in unique:
                    if self.values.count(val) == 4:
                        # Found Four of a kind
                        if args.verbose: print 'Found a Four of a Kind!'
                        return 'Four of a Kind'
                    # End if
                # End for

                for val in unique:
                    if self.values.count(val) == 3:
                        trip = val
                        for value in unique:
                            if value == trip:
                                continue
                            elif self.values.count(value) == 2:
                                # Found Full House
                                if args.verbose: print 'Found a Full House!'
                                return 'Full House'
                            # End if/else block
                        # End for

                        if not straight:
                            # Found Three of a Kind
                            if args.verbose: print 'Found Three of a Kind!'
                            return 'Three of a Kind'
                    # End if
                # End for

                if straight:
                    # Found Straight
                    if args.verbose: print 'Found a Straight!'
                    return 'Straight'
                # End if

                for val in unique:
                    if self.values.count(val) == 2:
                        dub = val
                        for value in unique:
                            if value == dub:
                                continue
                            elif self.values.count(value) == 2:
                                # Found Two Pair
                                if args.verbose: print 'Found a Two Pair!'
                                return 'Two Pair'
                            # End if/else block
                        # End for

                        # Found a Pair
                        if args.verbose: print 'Found a Pair!'
                        return 'Pair'
                    # End if
                # End for
            # End else
            
            if args.verbose: print 'Found a High Card!'
            return 'High Card'
        # End def
    # End class

    def __init__(self):
        if args.verbose: print 'Generating a deck of cards to use...'
        self.suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        self.values = range(1, 14)
        self.names = [ 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        self.deck = []
        for suit in self.suits:
            for i, value in enumerate(self.values):
                self.deck.append( deck.card(suit, value, self.names[i]) )
            # End for
        # End for
        if args.verbose:
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

    def get_hand(self, num_cards):
        hand_list = []

        for i in range(num_cards):
            rand = secure_random.choice(self.deck)
            while rand in hand_list:
                rand = secure_random.choice(self.deck)
            # End while

            hand_list.append(rand)
        # End for

        return deck.hand(hand_list)
    # End def
# End class


def main():
    start_time = time.time()

    if not args.num_hands:
        print 'You must supply a value for the number of hands you wish to run this statistical analysis on.'
        sys.exit()
    # End if

    if not args.num_cards:
        print 'You must supply a value for the number of cards you wish to draw per hand.'
        sys.exit()
    # End if

    if not args.multiprocessing:
        results = do_work(args.num_cards, args.num_hands)
    else:
        results = {}
        work_queue = Queue()
        processes = []

        remainder = args.num_hands % args.multiprocessing
        work = (args.num_hands - remainder) / args.multiprocessing

        for i in range(args.multiprocessing):
            if i == 0:
                processes.append(Process(target=do_work, args=(args.num_cards, work + remainder, work_queue)))
            else:
                processes.append(Process(target=do_work, args=(args.num_cards, work, work_queue)))
        # End for

        for p in processes:
            p.start()
        # End for

        for p in processes:
            p.join()
        # End for

        while not work_queue.empty():
            res = work_queue.get()
            for key in res:
                if key in results:
                    results[key] += res[key]
                else:
                    results[key] = res[key]
                # End if/else block
            # End for
        # End while
    # End if/else block

    sorted_res = sorted(results.items(), key=itemgetter(1))
    # List of tuples: ('Name of Match', number_of_occurances)

    print 'The results of %s consecutive %s card draws are as follows: \n' % (args.num_hands, args.num_cards)
    for item in sorted_res:
        print '%10s - %11s\t(%5.2f %%)' % (item[1], item[0], ((float(item[1]) / float(args.num_hands)) * 100) )
    # End for

    print "\n"
    print "--- Generated in %.4f seconds ---" % (time.time() - start_time)
# End def

def do_work(cards=0, hands=0, queue=None):
    card_deck = deck()

    results = {}

    for i in range(hands):
        if args.verbose: print 'Drawing hand #%s...' % (i)
        cur_hand = card_deck.get_hand(cards)
        res = cur_hand.score()

        if res not in results.keys():
            results[res] = 1
        else:
            results[res] += 1
        # End if/else block
    # End for

    if not queue:
        return results
    else:
        queue.put(results)
        return
    # End if/else block
# End def

if __name__ == '__main__':
    main()
# End if
