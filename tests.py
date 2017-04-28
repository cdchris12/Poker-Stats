from deck import deck

def logic_test(verbose=False):
    # Suit, Value, Name
    if verbose: print 'Testing Royal Flush...'
    r_flush = deck.hand([
    deck.card('Spades', 1, 'Ace'),
    deck.card('Spades', 13, 'King'),
    deck.card('Spades', 12, 'Queen'),
    deck.card('Spades', 11, 'Jack'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = r_flush.score()
        expected = "Royal Flush"
        assert res == expected
    except Exception, e:
        print res
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block
    # Testing Royal Flush logic

    if verbose: print 'Testing Royal Flush with Four of a Kind...'
    r_flush.add([
    deck.card('Hearts', 1, 'Ace'),
    deck.card('Diamonds', 1, 'Ace'),
    deck.card('Clubs', 1, 'Ace'),
    ])
    try:
        res = r_flush.score()
        expected = "Royal Flush"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block
    # Verifying Royal Flush comes before Four of a Kind

    if verbose: print 'Testing Straight Flush...'
    s_flush = deck.hand([
    deck.card('Spades', 9, 'Nine'),
    deck.card('Spades', 13, 'King'),
    deck.card('Spades', 12, 'Queen'),
    deck.card('Spades', 11, 'Jack'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = s_flush.score()
        expected = "Straight Flush"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block

    if verbose: print 'Testing Flush...'
    flush = deck.hand([
    deck.card('Spades', 9, 'Nine'),
    deck.card('Spades', 13, 'King'),
    deck.card('Spades', 3, 'Three'),
    deck.card('Spades', 11, 'Jack'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = flush.score()
        expected = "Flush"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block

    if verbose: print 'Testing Four of a Kind...'
    four_kind = deck.hand([
    deck.card('Spades', 9, 'Nine'),
    deck.card('Diamonds', 9, 'Nine'),
    deck.card('Hearts', 9, 'Nine'),
    deck.card('Clubs', 9, 'Nine'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = four_kind.score()
        expected = "Four of a Kind"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block

    if verbose: print 'Testing Full House...'
    f_house = deck.hand([
    deck.card('Spades', 9, 'Nine'),
    deck.card('Diamonds', 9, 'Nine'),
    deck.card('Hearts', 10, 'Ten'),
    deck.card('Clubs', 10, 'Ten'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = f_house.score()
        expected = "Full House"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block

    if verbose: print 'Testing Three of a Kind...'
    three_kind = deck.hand([
    deck.card('Spades', 9, 'Nine'),
    deck.card('Diamonds', 9, 'Nine'),
    deck.card('Hearts', 9, 'Nine'),
    deck.card('Clubs', 11, 'Jack'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = three_kind.score()
        expected = "Three of a Kind"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block

    if verbose: print 'Testing Two Pair...'
    two_pair = deck.hand([
    deck.card('Spades', 9, 'Nine'),
    deck.card('Diamonds', 9, 'Nine'),
    deck.card('Hearts', 8, 'Eight'),
    deck.card('Clubs', 8, 'Eight'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = two_pair.score()
        expected = "Two Pair"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block

    if verbose: print 'Testing Pair...'
    pair = deck.hand([
    deck.card('Spades', 9, 'Nine'),
    deck.card('Diamonds', 9, 'Nine'),
    deck.card('Hearts', 8, 'Eight'),
    deck.card('Clubs', 11, 'Jack'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = pair.score()
        expected = "Pair"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block

    if verbose: print 'Testing High Card...'
    h_card = deck.hand([
    deck.card('Spades', 3, 'Three'),
    deck.card('Diamonds', 9, 'Nine'),
    deck.card('Hearts', 8, 'Eight'),
    deck.card('Clubs', 11, 'Jack'),
    deck.card('Spades', 10, 'Ten'),
    ], verbose)
    try:
        res = h_card.score()
        expected = "High Card"
        assert res == expected
    except Exception, e:
        print 'Expected "', expected,'", got " ', res, '" instead.'
        return False
    else:
        if verbose: print 'PASSED!!!\n'
    # End try/except/else block

    return True
# End def
