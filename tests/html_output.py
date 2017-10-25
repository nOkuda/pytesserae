"""Converts the output of the search function to html code"""
import re

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

    return output
