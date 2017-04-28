#!/usr/bin/python

import argparse
import sys
import time
import os
from deck import deck
from tests import logic_test

from operator import itemgetter
from multiprocessing import Pool, TimeoutError, cpu_count, Process, Queue

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num_hands', type=int, help='The number of hands to simulate drawing.')
parser.add_argument('-c', '--num_cards', type=int, choices=range(1, 14), help='The number of cards to draw each hand. Must be between 5 and 13.')
parser.add_argument('-m', '--multiprocessing', type=int, default=0, choices=range(2, cpu_count()+1), help='Enter the degree of multiprocessing you\'d like to use for significantly faster computation of large statistical analyses.')
parser.add_argument('-t', '--testing', action='store_true', help='Run test suite.')
parser.add_argument('-v', '--verbose', action='store_true', help='Show more information as the results are being computed.')
args = parser.parse_args()

def main():
    start_time = time.time()

    if args.testing:
        res = logic_test(args.verbose)
        if res:
            print 'Testing passed!!!'
        else:
            print 'Testing failed!!!'
        # End if/else block
        sys.exit(0)
    # End if

    if not args.num_hands:
        print 'You must supply a value for the number of hands you wish to run this statistical analysis on.'
        sys.exit()
    # End if

    if not args.num_cards:
        print 'You must supply a value for the number of cards you wish to draw per hand.'
        sys.exit()
    # End if

    if not args.multiprocessing:
        results = do_work(args.num_cards, args.num_hands, args.verbose)
    else:
        results = {}
        work_queue = Queue()
        processes = []

        remainder = args.num_hands % args.multiprocessing
        work = (args.num_hands - remainder) / args.multiprocessing

        for i in range(args.multiprocessing):
            if i == 0:
                processes.append(Process(target=do_work, args=(args.num_cards, work + remainder, args.verbose, work_queue, i + 1)))
            else:
                processes.append(Process(target=do_work, args=(args.num_cards, work, args.verbose, work_queue, i + 1)))
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

def do_work(cards=0, hands=0, verbose=False, queue=None, _id=1):
    card_deck = deck(verbose)

    results = {}

    for i in range(hands):
        if verbose: print 'Drawing hand #%s...' % (i * _id)
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
