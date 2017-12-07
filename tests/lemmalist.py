import argparse
import re
import math
import tfidf as tf
import cltk
from cltk.corpus.utils.importer import CorpusImporter
corpus_importer = CorpusImporter('Latin')
corpus_importer.list_corpora
corpus_importer.import_corpus('latin_models_cltk')
from cltk.stem.lemma import LemmaReplacer
lemmatizer = LemmaReplacer('latin')

class Tess:
    """A class for tokens and lines of .tess files"""

    def __init__(self, word, index, number): # form of word, line number, position in line
        self.word = word
        self.index = index
        self.number = number
        

def wordlist(text):
    #identify stop words
    topsource = tf.readfile(text)
    toptenSource = tf.topten(topsource)

    # create token list from source text
    with open(text, 'r') as f:
        tessTokens = []
        for line in f:
            line = line.lower()
            result = re.search("^<.*\>", line)
            if result:
                tag = result.group()
            line = re.sub("^<.*\>", "", line)  #removes tess line indexing
            line = re.sub("[\-\t\n]", "", line)
            line = re.sub("[^\w\s]", " ", line)
            line = re.sub("[^A-Za-z ]", "", line) # removes punctuation
            tokens = lemmatizer.lemmatize(line.split(" "))
            for t in tokens:
                if t not in toptenSource:
                    if re.search("[A-Za-z ]", t):
                        indexT = Tess(t, tag, 0)
                        tessTokens.append(indexT)
        return(tessTokens)

            # score.py: rank matches
            # use parse_highlight to mark each match in both contexts
            # add both marked lines to match list
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates word list')
    parser.add_argument("text", help="source text")
    args = parser.parse_args()
    intext = args.text
    

    wordlist(intext)
