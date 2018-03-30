import argparse
import re
import math
import tfidf as tf

def _parse_args():
    parser = argparse.ArgumentParser(
        description='Cleans up and tokenizes a text')
    parser.add_argument(
        'text',
        help='Some text')
    return parser.parse_args()

def _run():
    args = _parse_args()
    tokens = wordlist(args.text)
    print(tokens)

def wordlist(text):
    #identify stop words
    topsource = tf.readfile(text)
    toptenSource = tf.topten(topsource)

    # create token list from source text
    with open(text, 'r') as f:
        all_tokens = []
        for line in f:
            line = line.lower()
            result = re.search("^<.*\>", line)
            if result:
                tag = result.group()
            line = re.sub("^<.*\>", "", line)  #removes tess line indexing
            line = re.sub("[\-\t\n]", "", line)
            line = re.sub("[^\w\s]", " ", line)
            line = re.sub("[^A-Za-z ]", "", line) # removes punctuation
            tokens = line.split(" ")
            all_tokens.append(tokens)
        return(all_tokens)

if __name__ == '__main__':
    _run()
