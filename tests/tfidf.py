#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

notes:

    The following program is designed to create stop-word lists for texts being
    used in Tesserae. There are several methods, including methods for deriving
    longer and shorter stop-word lists. These methods are strictly for
    experimentation and are available if the need for them arises in the future

    However, the most important method is the following:
        ***This method produces the stop word list***
       
        tenstopwords(doc001, doc002)
            
            parameters: (file.tess, file.tess)
        This method takes two text files of the .tess format as its paramaters,
        and produces a list of ten stop words to be removed from the first
        document, doc001.
        

    Additional Methods:
        
        a)readfile(doc) - paramaters: (file.tess); returns a
    dictionary of word-frequency pairs; used by all other methods
        b)topten(frequencydictionary) - parameters:(word-frequency dictionary);
    returns a list of ten most frequent words from a word frequency dictionary
        c)topx(frequencydictionary, x) - parameters: (word-frequency dictionary
    , integer); returns a list of x-length of the most frequent words from the
    frequency dictionary
        d)tfidf(docmen1, docmen2) - parameters(file.tess, file.tess); produces
    tfidf dictionary of words in docmen1
    
        e)
    
    For information on the tfidf please see:
        https://en.wikipedia.org/wiki/Tf%E2%80%93idf
        
Created on Sat Oct 28 18:37:18 2017
@author: mitchellkristie
"""
import re
import math

"""Reads .tess file; creates word-frequency dictionary"""
def readfile(doc):
    freqdict = dict()
    with open(doc, encoding='utf-8') as f:
        for line in f:
            line = line.lower()
            line = re.sub("^<.*\>", "", line)  #removes tess line indexing
            line = re.sub("-", "", line)
            line = re.sub("[^\w\s]", " ", line)
            line = line.rsplit()  #returns list of the words in the line
            for word in line:  #creates raw word count
                if word in freqdict.keys():
                    freqdict[word] = freqdict[word] + 1
                else:
                    freqdict[word] = 1
        wordcount = math.fsum(freqdict.values())
        for word in freqdict.keys():  #creates frequency dictionary
            freqdict[word] = (freqdict[word]/wordcount)

        return freqdict

"""Reads frequency dictionary; returns top ten most frequent words"""
def topten(frequencydictionary):
    sort = sorted(frequencydictionary,
                  key=frequencydictionary.__getitem__,
                  reverse=True)
    return sort[0:10]

""" Returns stop-word list of x length"""
def topx(frequencydictionary, x):
    sort = sorted(frequencydictionary,
                  key=frequencydictionary.__getitem__,
                  reverse=True)
    return sort[0:x]

"""Reads two .tess files; Returns tfidf list of .tess file docmen1""" 
def tfidf(docmen1, docmen2):
    freqdict1 = readfile(docmen1)
    freqdict2 = readfile(docmen2)
    tfidf1 = dict()
    for key in freqdict1:
        if key not in freqdict2:
            x = 1
        else:
            x = 2
            tfidf1[key] = (math.log((freqdict1.get(key)))) * math.log(1+(2/x))
    return tfidf1

"""Returns list of ten stop words for doc01"""
def tenstopwords(doc01, doc02):
    return topten(tfidf(doc01, doc02))

"""Returns list stop word list of x length, for doc001"""
def xstopwords(doc001, doc002, x):
    return topx(tfidf(doc001, doc002), x)
