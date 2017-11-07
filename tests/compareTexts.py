"""Compares two texts"""
import argparse
import re

def compare(source, target):
    # remove punctuation/capitalization?
    # create token list from source text
    with open(source, 'r') as f:
        token1 = []
        for line in f:
            line = line.lower()
            line = re.sub("^<.*\>", "", line)  #removes tess line indexing
            line = re.sub("[-\t\n]", "", line)
            line = re.sub("[^\w\s]", " ", line)
            tokens = line.split(" ")
            for t in tokens:
                if t not in token1:
                    token1.append(t)

    # create token list from target text
    with open(target, 'r') as g:
        token2 = []
        for line in g:
            line = line.lower()
            line = re.sub("^<.*\>", "", line)  #removes tess line indexing
            line = re.sub("[-\t\n]", "", line)
            line = re.sub("[^\w\s]", " ", line)
            tokens = line.split(" ")
            for t in tokens:
                if t not in token2:
                    token2.append(t)

    # delete stop words from both lists?

    matches = []
    # compare each element in token1 with elements in token2, return matches
    for x in token1:
        if x in token2:
            matches.append(x)
            # give more weight to rarer word and longer phrase matches
            # connect matches back to original contexts
            # use parse_highlight to mark each match in both contexts
            # add both marked lines to match list

    print(matches)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two texts')
    parser.add_argument("text1", help="source text")
    parser.add_argument("text2", help="target text")
    args = parser.parse_args()
    source = args.text1
    target = args.text2

    compare(source, target)

