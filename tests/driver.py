import parse_highlight
import html_output
import argparse

parser = argparse.ArgumentParser(description='Search file for regex')
parser.add_argument("inputFile", help="name of file to search")
parser.add_argument("search", help="expression to search for")
args = parser.parse_args()
fileName = args.inputFile
search = args.search

matchList = parse_highlight.searchify(fileName, search)
output = html_output.html(matchList)

with open('SearchResult.html', 'w') as f:
    for l in output:
        f.write(l + '</br>')
