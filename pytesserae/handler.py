"""A function to prepare .tess texts for analysis"""
import re


def tokenize(line):
    """Normalizes and tokenizes a line from a .tess file

    Capital letters are changed to lowercase, line numbering and
    extraneous whitespace is removed, and the result is given as
    a list of tokens.

    The tokenizer is intended to be applied to a line from a .tess
    file at a later point, e.g.:

    with open('example.tess', 'r') as text:
        for line in text:
            tokens = handler.tokenize(line)
            ...

    The resulting tokens can then be passed, along with that of
    another file's line, into the matching function, and the result
    of that used in the scoring process.

    Parameters
    ----------
    line : str
        Line from a .tess file to be cleaned up and tokenized

    Returns
    -------
    [str]
        A list containing each token in the line

    """
    tokens = line.lower()
    # removes line indexing
    tokens = re.sub(r'^<.*\>', '', tokens)
    tokens = re.sub(r'[\-\t\n]', '', tokens)
    tokens = re.sub(r'[^\w\s]', '', tokens)
    # removes punctuation
    tokens = re.sub(r'[^A-Za-z ]', '', tokens)
    tokens = tokens.split(' ')
    return tokens
