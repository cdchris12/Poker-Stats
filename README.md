# Poker-Stats
A Python program which provides statistics of winning poker hands over a definied number of draws and a defined number of cards drawn. Works with or without native Python multiprocessing.

### Usage
This script can be ran by supplying the required number of cards and hands, at a minimum:

`python card_probs.py -c 5 -n 10000`

or

`./card_probs.py --num_cards 10 --num_hands 500000`

#### Testing
This script has a built in testing suite, which you can call with the `-t` switch:

`python card_probs.py -t`

or

`./card_probs.py --testing`

#### Multithreading
This script supports native multiprocessing via the `-m` switch, which significantly reduces runtime:

`python card_probs.py -c 7 -n 6070000 -m`

or

`./card_probs.py --num_cards 15 --num_hands 5000000 --multiprocessing`

#### Verbosity
If, for some reason, you want to see a lot of info about what's happening when you run the script, it supports increasing output verbosity via the `-v` switch. **_USE WITH CAUTION_**:

`python card_probs.py -c 7 -n 60700 -m -v`

or

`./card_probs.py --num_cards 15 --num_hands 12000000 --multiprocessing --verbose`
