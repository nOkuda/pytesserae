import argparse
import re
parser = argparse.ArgumentParser(description='Search file for reg expression.')
parser.add_argument("inputFile", help="name of file to search")
parser.add_argument("search", help="expression to search for")
args = parser.parse_args()
filePath = args.inputFile
searchTerm = args.search


def searchify():
    with open(filePath, 'r') as f:
        foundLines = []
        for line in f:
            result = re.search(searchTerm, line)
            if result:
                literal = result.group()
                highlight = line.replace(literal, '*{}*'.format(literal))
                foundLines.append(highlight)
                return(foundLines)


searchify()
