import argparse
import re

def searchify(filePath, searchTerm):
    with open(filePath, 'r') as f:
        foundLines = []
        for line in f:
            result = re.search(searchTerm, line)
            if result:
                literal = result.group()
                highlight = line.replace(literal, '*{}*'.format(literal))
                foundLines.append(highlight)
        return(foundLines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search file for regex')
    parser.add_argument("inputFile", help="name of file to search")
    parser.add_argument("search", help="expression to search for")
    args = parser.parse_args()
    file = args.inputFile
    search = args.search
        
    searchify(file, search)
