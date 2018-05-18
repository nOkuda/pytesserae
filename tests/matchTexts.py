"""
File: matchTexts.py
Authors: Joe Baiz and Liz Soper
Date: 2/7/18
Description: Takes two texts, creates a dictionary for each (see dictionary.py), and returns a list of matched words (highlighted in their contexts).
"""
import argparse
import re
import dictionary as dictn
import html_output as html

def compare(source, target):
    tokens1 = dictn.wordlist(source)
    tokens2 = dictn.wordlist(target)
    matches = []
    for sourceLineID,sourceWords in tokens1.items():
        for word1 in sourceWords:
            for targetLineID,targetWords in tokens2.items():
                for word2 in targetWords:
                    if word1==word2:
                        sourceMatch=str(sourceWords).replace(word1,'*{}*'.format(word1))
                        matches.append(sourceLineID+sourceMatch)
                        targetMatch=str(targetWords).replace(word2,'*{}*'.format(word2))
                        matches.append(targetLineID+targetMatch)
    html.html(matches)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two texts')
    parser.add_argument("text1", help="source text")
    parser.add_argument("text2", help="target text")
    args = parser.parse_args()
    source = args.text1
    target = args.text2

    compare(source, target)
