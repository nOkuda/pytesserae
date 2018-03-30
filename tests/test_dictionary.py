from collections import Counter
import argparse

#source = ['banana', 'Rui Chaves', 'Rui Chaves']
#target = ['Mickey Mouse', 'Rui Chaves', 'banana']

def _parse_args():
    parser = argparse.ArgumentParser(
        description='Find matching terms between two texts')
    parser.add_argument(
        'source',
        help='The starting point for allusion-finding')
    parser.add_argument(
        'target',
        help='The text in which one hopes to find allusions')
    return parser.parse_args()

def _run():
    args = _parse_args()
    print_matches(eval(args.source), eval(args.target))

def matchify(source, target):
    # Returns matched tokens from two texts w/ the frequencies of each
    source_dict = Counter(source)
    target_dict = Counter(target)
    # Creates dictionaries of frequencies indexed by tokens
    matches = list(set(source).intersection(target))
    # Creates a list of matches
    return(matches)

def print_matches(source, target):
    matches = matchify(source, target)
    print(matches)

def countify(source, target):
    matches = matchify(source, target)
    source_dict = Counter(source)
    target_dict = Counter(target)
    i = 0
    for token in source_dict:
        if token in matches:
            print({token: source_dict[token]})
#    for match in matches:
#        # Prints the num of occurences of each item in matches
#        print(source_dict[matches[i]])
#        print(target_dict[matches[i]])
#        i =+ 1

def frequency(source, target):
    matches = matchify(source, target)
    print(Counter(matches))

if __name__ == '__main__':
    _run()
