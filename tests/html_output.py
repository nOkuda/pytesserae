"""Converts the output of the search function to html code"""
import re
import argparse

def html(matchList):
    output = []
    for l in matchList:
        # locate match in asterisks
        match = re.search(r'\*[a-zA-Z]+\*', l)
        markedMatch = match.group()
        # highlight remaining match
        highlight = l.replace(markedMatch, '<span style="color: red">{}</span>'.format(markedMatch))
        # remove asterisks
        highlight = highlight.replace("*", "")
        output.append(highlight)

    return(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Format list of tokens in html')
    parser.add_argument("tokens", help="list of tokens")
    args = parser.parse_args()
    matches = args.tokens

    html(matches)
    print(output)
