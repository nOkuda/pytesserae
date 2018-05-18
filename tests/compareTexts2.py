import argparse
import re
import math
import tfidf as tf

class Tess:
    """A class for tokens and lines of .tess files"""

    def __init__(self, word, index, number): # form of word, line number, position in line
        self.word = word
        self.index = index
        self.number = number
        

def compare(source, target):
    #identify stop words
    topsource = tf.readfile(source)
    toptarget = tf.readfile(target)
    toptenSource = tf.topten(topsource)
    toptenTarget = tf.topten(toptarget)

    # create token list from source text
    with open(source, 'r') as f:
        token1 = []
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
            for t in tokens:
                if t not in toptenSource:
                    if re.search("[A-Za-z ]", t):
                        indexT = Tess(t, tag, 0)
                        if indexT not in token1:
                            token1.append(indexT)

    # create token list from target text
    with open(target, 'r') as g:
        token2 = []
        for line in g:
            line = line.lower()
            result = re.search("^<.*\>", line)
            if result:
                tag = result.group()
            line = re.sub("^<.*\>", "", line)  #removes tess line indexing
            line = re.sub("[\-\t\n]", "", line)
            line = re.sub("[^\w\s]", " ", line)
            line = re.sub("[^A-Za-z ]", "", line) # removes punctuation
            tokens = line.split(" ")
            for t in tokens:
                if t not in toptenTarget:
                    if re.search("[A-Za-z ]", t):
                        indexT = Tess(t, tag, 0)
                        if indexT not in token2:
                            token2.append(indexT)

    # compare each element in token1 with elements in token2, return matches
    matches1 = []
    matches2 = []

    # lemmatize every x.word in token1 and token2
    for x in token1:
        for y in token2:
            if x.word == y.word:
                if x not in matches1:
                    matches1.append(x)
                if y not in matches2:
                    matches2.append(y)
            # score.py: rank matches
            # use parse_highlight to mark each match in both contexts
            # add both marked lines to match list
    for m in matches1 and matches2:
        print(m.word)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two texts')
    parser.add_argument("text1", help="source text")
    parser.add_argument("text2", help="target text")
    args = parser.parse_args()
    source = args.text1
    target = args.text2

    compare(source, target)
