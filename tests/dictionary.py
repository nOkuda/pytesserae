"""
File: dictionary.py
Authors: Joe Baiz and Liz Soper
Date: 2/7/18
Description: Takes one text file argument and returns a dictionary of tokens, omitting stop words (see tfidf.py).

"""
import argparse
import re
import math
import tfidf as tf

def wordlist(text):
    # identify stop words
    topsource = tf.readfile(text)
    toptenSource = tf.topten(topsource)

    # create dictionary by line: {'lineID': [wordsInLine],...}
    with open(text, 'r') as f:
        tessTokens = []
        dictionary={}
        for line in f:
            line = line.lower()
            result = re.search("^<.*\>", line)
            if result:
                lineID = result.group()
            line = re.sub("^<.*\>", "", line)  #remove line ID
            line = re.sub("[\s+]", " ", line)
            line = re.sub("[^A-Za-z ]", "", line) # removes punctuation
            tessTokens=line.split()
            for word in tessTokens:
                if word in toptenSource:
                    tessTokens.remove(word)
            dictionary[lineID]=tessTokens
        return(dictionary)
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates dictionary')
    parser.add_argument("text", help="source text")
    args = parser.parse_args()
    intext = args.text
    

    print(wordlist(intext))
