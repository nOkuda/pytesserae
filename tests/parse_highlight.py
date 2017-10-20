import argparse
import re
parser = argparse.ArgumentParser(description='Search a file for a regular expression.')
parser.add_argument("inputFile", help="name of file to search")
parser.add_argument("search", help="expression to search for")
args = parser.parse_args()
filePath = args.inputFile
searchTerm = args.search


def searchify():
    with open(filePath, 'r') as f:
        with open('searchResult.html', 'w', encoding='utf-8') as g:
            foundLines = []
            for line in f:
                result = re.search(searchTerm, line)
                if result:
                    literal = result.group()
                    highlight = line.replace(literal, '<span style="color:red">{}</span>'.format(literal))
                    foundLines.append(highlight+'</br>')
            if len(foundLines) == 0:
                g.write("No matches found.")
            else:
                for l in foundLines:
                    g.write(l)


searchify()
