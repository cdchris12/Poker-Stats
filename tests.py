from deck import deck

def run_test(t_hand, expected, verbose=False):
    if verbose: print 'Testing %s...' % expected
    try:
        res = t_hand.score()
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print '%s Testing PASSED!!!\n' % expected
    # End try/except/else block
# End def

def logic_test(verbose=False):
    # Suit, Value, Name
    run_test(
        deck.hand([
            deck.card('Spades', 1, 'Ace'),
            deck.card('Spades', 13, 'King'),
            deck.card('Spades', 12, 'Queen'),
            deck.card('Spades', 11, 'Jack'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'Royal Flush',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 1, 'Ace'),
            deck.card('Spades', 13, 'King'),
            deck.card('Spades', 12, 'Queen'),
            deck.card('Spades', 11, 'Jack'),
            deck.card('Spades', 10, 'Ten'),
            deck.card('Hearts', 1, 'Ace'),
            deck.card('Diamonds', 1, 'Ace'),
            deck.card('Clubs', 1, 'Ace'),
        ], verbose),
        'Royal Flush',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 9, 'Nine'),
            deck.card('Spades', 13, 'King'),
            deck.card('Spades', 12, 'Queen'),
            deck.card('Spades', 11, 'Jack'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'Straight Flush',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 9, 'Nine'),
            deck.card('Spades', 13, 'King'),
            deck.card('Spades', 3, 'Three'),
            deck.card('Spades', 11, 'Jack'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'Flush',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 9, 'Nine'),
            deck.card('Diamonds', 9, 'Nine'),
            deck.card('Hearts', 9, 'Nine'),
            deck.card('Clubs', 9, 'Nine'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'Four of a Kind',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 9, 'Nine'),
            deck.card('Diamonds', 9, 'Nine'),
            deck.card('Hearts', 10, 'Ten'),
            deck.card('Clubs', 10, 'Ten'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'Full House',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 9, 'Nine'),
            deck.card('Diamonds', 9, 'Nine'),
            deck.card('Hearts', 9, 'Nine'),
            deck.card('Clubs', 11, 'Jack'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'Three of a Kind',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 9, 'Nine'),
            deck.card('Diamonds', 9, 'Nine'),
            deck.card('Hearts', 8, 'Eight'),
            deck.card('Clubs', 8, 'Eight'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'Two Pair',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 9, 'Nine'),
            deck.card('Diamonds', 9, 'Nine'),
            deck.card('Hearts', 8, 'Eight'),
            deck.card('Clubs', 11, 'Jack'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'Pair',
    verbose)

    run_test(
        deck.hand([
            deck.card('Spades', 3, 'Three'),
            deck.card('Diamonds', 9, 'Nine'),
            deck.card('Hearts', 8, 'Eight'),
            deck.card('Clubs', 11, 'Jack'),
            deck.card('Spades', 10, 'Ten'),
        ], verbose),
        'High Card',
    verbose)

    return True
# End def
