"""Compares two texts"""
import argparse
import re

def compare(source, target):
    # remove punctuation/capitalization?
    # create token list from source text
    with open(source, 'r') as f:
        token1 = []
        for line in f:
            token1.append(line.split(str=r"\b"))

    # create token list from target text
    with open(target, 'r') as g:
        token2 = []
        for line in g:
            token2.append(line.split(str=r"\b"))

    # delete stop words from both lists?

    matches = []
    # compare each element in token1 with elements in token2, return matches
    for x in token1:
        for y in token2:
            if(x == y)
               # somehow connect x and y back to original contexts?
               # use parse_highlight to mark each match in both contexts
               # add both marked lines to match list

    return(matches)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two texts')
    parser.add_argument("text1", help="source text")
    parser.add_argument("text2", help="target text")
    args = parser.parse_args()
    source = args.text1
    target = args.text2

    compare(source, target)

