import argparse
import re
import compareTexts3 as comp

def compare(source, target):
    tokens1 = comp.wordlist(source)
    tokens2 = comp.wordlist(target)
    matches = []
    for x in tokens1:
        for y in tokens2:
            if x.word == y.word:
                matches.append(x)
                matches.append(y)
    return(matches)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two texts')
    parser.add_argument("text1", help="source text")
    parser.add_argument("text2", help="target text")
    args = parser.parse_args()
    source = args.text1
    target = args.text2

    compare(source, target)
